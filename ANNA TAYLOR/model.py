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
    suggested_gender: str
    images: List[str]
    all_size: List[str]
    selected_size: str
    description: str
    product_detailes: Dict[str, str]  
    rating: str
    reviews: str
    product_varients: List[ProductVariant]