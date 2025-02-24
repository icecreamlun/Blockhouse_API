from fastapi import FastAPI, WebSocket, WebSocketDisconnect, BackgroundTasks
from pydantic import BaseModel
from typing import List
import uvicorn
import asyncio

from app.database import get_db, SessionLocal, Base
from app.models import Order
from app.schemas import OrderCreate, OrderRead

# control all the connections
connected_websockets: List[WebSocket] = []

def create_tables():
    db = SessionLocal()
    Base.metadata.create_all(bind=db.bind)
    db.close()

app = FastAPI(title="Trade Orders API")

@app.on_event("startup")
def on_startup():
    create_tables()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time updates
    """
    await websocket.accept()
    connected_websockets.append(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        connected_websockets.remove(websocket)

async def notify_all_clients(order: Order):
    """
    Notify all connected clients about new order
    """
    message = {
        "action": "new_order",
        "data": {
            "id": order.id,
            "symbol": order.symbol,
            "price": order.price,
            "quantity": order.quantity,
            "order_type": order.order_type,
        }
    }
    for ws in connected_websockets:
        try:
            await ws.send_json(message)
        except:
            connected_websockets.remove(ws)

@app.post("/orders", response_model=OrderRead, status_code=201)
async def create_order(order_data: OrderCreate, background_tasks: BackgroundTasks):
    """
    Create new order and notify connected clients
    """
    db = get_db()
    new_order = Order(**order_data.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    db.close()

    # Notify clients about new order
    await notify_all_clients(new_order)
    
    return new_order

@app.get("/orders", response_model=List[OrderRead])
def list_orders():
    db = get_db()
    orders = db.query(Order).all()
    db.close()
    return orders

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)