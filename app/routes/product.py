from fastapi import APIRouter, Depends, HTTPException
from app.models.product import create_product, fetch_products
from app.schemas.product import ProductCreate, Product
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/")
def add_product(product: ProductCreate, user: dict = Depends(get_current_user)):
    product_id = create_product(product.name, product.price, user["id"])
    return {"id": product_id, **product.dict()}

@router.get("/")
def get_products():
    products = fetch_products()
    return products