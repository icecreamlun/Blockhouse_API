from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    order_type = Column(String, nullable=False)
