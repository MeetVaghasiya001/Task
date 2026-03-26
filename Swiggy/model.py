from pydantic import BaseModel
from typing import Dict,List,Optional


class ItemDetails(BaseModel):
    id : str 
    item : str = None ,
    short_description : Optional[str] = None
    brand : str = None
    images : Optional[List[str]] = None
    total_price : int = 0
    offer_price : Optional[int] = 0
    discount_value : Optional[int] = 0
    dicount : Optional[str] = None
    weight : Optional[float] = 0
    

class Item(BaseModel):
    items : Dict[str,List[ItemDetails]]