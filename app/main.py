from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from app.database import get_db, SessionLocal, Base
from app.models import Order
from app.schemas import OrderCreate, OrderRead
import uvicorn

# Create the database (if it doesn't exist) on startup
def create_tables():
    db = SessionLocal()
    Base.metadata.create_all(bind=db.bind)
    db.close()

app = FastAPI(title="Trade Orders API")

@app.on_event("startup")
def on_startup():
    create_tables()

@app.post("/orders", response_model=OrderRead, status_code=201)
def create_order(order_data: OrderCreate):
    db = get_db()
    new_order = Order(**order_data.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    db.close()
    return new_order

@app.get("/orders", response_model=List[OrderRead])
def list_orders():
    db = get_db()
    orders = db.query(Order).all()
    db.close()
    return orders

# (Bonus) WebSocket support for real-time updates could be added here.

"""
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Example: Send a simple periodic update or fetch updates from DB.
        data = {"message": "Order status update..."}
        await websocket.send_json(data)
        # Add logic to break or keep going...
"""

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
