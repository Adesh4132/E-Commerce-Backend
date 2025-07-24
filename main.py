from fastapi import FastAPI
from .database import Base, engine
from .routers import users, products, orders

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Commerce Backend API")

# Register routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
