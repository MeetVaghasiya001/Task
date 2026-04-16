from pydantic import BaseModel
from typing import List, Dict


class ProductVariant(BaseModel):
    sku: str
    color: str
    price: float
    currency: str


class Product(BaseModel):
    product_catagory_id: str
    name: str
    brand: str
    price:str
    suggested_gender: str
    selected_size: str
    description: str
    rating: str
    reviews: str
    images: List[str]
    all_size: List[str]
    product_detailes: Dict[str, str]  
    product_varients: List[ProductVariant]