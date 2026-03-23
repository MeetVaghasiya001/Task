from pydantic import BaseModel 
from typing import List,Optional

class Location(BaseModel):
    address : str
    street_address : str
    city : str 
    country : str
    postal_code : str 
    region : str 
    latitude : float
    longitude : float

class Item(BaseModel):
    name : Optional[str]
    description : Optional[str]
    price : Optional[int]
    avalible :Optional[bool]
    item_image : Optional[str]

   
class Menu(BaseModel):
    catagory : str
    item : List[Item]

class Uber(BaseModel):
    name : str 
    location :Location
    rating : Optional[float]
    cuisine : List[str]
    image:List[str]
    telephone : str
    menu : List[Menu]


