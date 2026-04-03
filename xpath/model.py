from pydantic import BaseModel
from typing import List,Dict,Any


class Book(BaseModel):
    name : str
    image:List[str]
    price : str
    stock : str 
    warning :str
    description : str
    product_information:Dict[str,Any]