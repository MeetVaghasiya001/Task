from pydantic import BaseModel
from typing import List,Dict,Optional,Any

class Price(BaseModel):
    name : str 
    value : int

class Product(BaseModel):
    item_name : str 
    subtitle : str 
    image : Optional[List[str]]
    brand : str 
    price : List[Price]
    rating : Optional[Dict[str,float]] = None
    product_highlights : Dict[Any,Any]
    manufacture : Dict[Any,Any]



