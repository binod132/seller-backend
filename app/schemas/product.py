from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float

class Product(BaseModel):
    id: int
    name: str
    price: float
    seller_id: int