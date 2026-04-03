from pydantic import BaseModel
from typing import List,Dict,Any


class Book(BaseModel):
    name : List[str]
    image:List[str]
    price : List[str]
    stock : str 
    warning : List[str]
    description : List[str]
    product_information:Dict[str,Any]