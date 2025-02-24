from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_order():
    order_data = {
        "symbol": "AAPL",
        "price": 150.0,
        "quantity": 100,
        "order_type": "BUY"
    }
    response = client.post("/orders", json=order_data)
    assert response.status_code == 201
    data = response.json()
    assert data["symbol"] == order_data["symbol"]
    assert data["price"] == order_data["price"]
    assert data["quantity"] == order_data["quantity"]
    assert data["order_type"] == order_data["order_type"]