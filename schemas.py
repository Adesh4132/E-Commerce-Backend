from pydantic import BaseModel
from typing import List
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

    class Config:
        orm_mode = True

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItemBase]

class OrderItemRead(OrderItemBase):
    id: int

    class Config:
        orm_mode = True

class OrderRead(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    items: List[OrderItemRead]

    class Config:
        orm_mode = True
