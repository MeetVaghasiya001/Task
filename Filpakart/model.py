from pydantic import BaseModel 
from typing import List,Dict,Any,Optional


class Price(BaseModel):
    value : Optional[int] = 0
    currency :Optional[str] =None

class Rating(BaseModel):
    rating : Optional[float] =0
    ratin_count : Optional[int] = 0
    review_count : Optional[int] = 0

class Seller(BaseModel):
    name : str 
    rating :Optional[float] 
    start : Optional[str] = None

class Product(BaseModel):
    name : Optional[str] = None 
    description :Optional[str] = None
    item_images : List[str]
    item_catagory : Optional[str] = None 
    brand : Optional[str] = None 
    price : Optional[Price] = None 
    ratings :Optional[Rating] = None 
    policy : Optional[str] = None 
    product_detailes : Dict[str,Any]
    seller_detailes : Optional[Seller] = None







