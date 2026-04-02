from pydantic import BaseModel
from typing import List,Dict,Optional,Any

class Varient(BaseModel):
    name : str 
    weight : str 
    price : int 
    is_selected : bool

class Product(BaseModel):
    name : str 
    brand : str 
    price : Optional[int] = 0 
    weight : Optional[str]
    currency : str 
    product_varient : List[Varient]
    Gallary : Dict[str,Optional[List[str]]]
    attributes : Dict[str,Any]