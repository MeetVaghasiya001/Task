from pydantic import BaseModel
from typing import List,Dict,Optional,Any


class Item(BaseModel):
    product_id : str
    product_skuId : str 
    product_name : str
    on_sale : str 
    price : float
    currency : str
    sale_price : Optional[float]
    product_images : List[str]
    colors : Optional[List[Dict[str,Any]]]

class Products(BaseModel):
    product : List[Item]