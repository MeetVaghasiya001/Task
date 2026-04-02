from pydantic import BaseModel
from typing import List,Dict,Optional,Any

class Items(BaseModel):
    name : str 
    decription : Optional[str] = None
    image : str
    weight : str 
    price : int 
    currency : str 
    store_id : int 
    stock : int 
    is_popular : Optional[bool]
    is_available : bool
    offer_price : Optional[List] = None


class Product(BaseModel):
    products : List[Items]