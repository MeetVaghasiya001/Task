from pydantic import BaseModel
from typing import List, Optional


class SKU(BaseModel):
    sku: str
    price: int
    size: str


class ColorOption(BaseModel):
    sku: str
    in_stock: bool
    color: str


class Product(BaseModel):
    product: str
    brand: str
    rating: int
    rating_count: int
    product_image: List[str]
    sku: str
    p_price: int
    discount_price: int
    catagory_id: List[str]
    color: str
    tages: Optional[str]
    product_detail: dict  
    policies: dict         
    color_option: Optional[List[ColorOption]]
    size: List[SKU]