from pydantic import BaseModel
from typing import List,Optional,Dict,Any


class Rating(BaseModel):
    rating : Optional[float] = 0
    rating_count : Optional[int] = 0
    recomend_count : Optional[int] = 0


class Size(BaseModel):
    a_id:int
    made_in:str 
    size:str
    price:Dict[str,int]
    chest_size:Optional[float]
    provider:str


class Colors(BaseModel):
    p_id:int
    product_name:str 
    rating : float
    review_count : int 
    final_price : int 
    total_price : int
    images : List[str]

class Product(BaseModel):
    id : int
    name : str
    description : str
    gender:str
    mrp : int 
    final_price:int
    discount_amount:int
    provider:str
    seller : Dict[str,str]
    images:List[str]
    reviews_rating : Optional[Rating]
    brand:str
    madeIn:str
    stock:str 
    product_specification:Dict[str,Any]
    technical_info:Dict[str,Any]
    benifits:Dict[str,Any]
    all_size:List[Size]
    other_options : List[Colors]




