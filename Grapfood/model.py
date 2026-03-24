from pydantic import BaseModel
from typing import List,Optional,Dict,Any

class Opning(BaseModel):
    open : bool
    displayedHours : Optional[str] = None
    sun : Optional[str] = None
    mon : Optional[str] = None
    tue : Optional[str] = None
    wed : Optional[str] = None
    thu : Optional[str] = None
    fri : Optional[str] = None
    sat : Optional[str] = None


class Combo(BaseModel):
    name : Optional[str] = None
    available : Optional[bool] = False
    price : Dict[str,Any] = None

class Modify(BaseModel):
    name : Optional[str] = None
    available : Optional[bool] = False
    all_modifires : Optional[List[Combo]]

class Item(BaseModel):
    name : Optional[str] = None 
    price : Optional[int] = 0
    image : Optional[str] = None 
    description: Optional[str] = None 
    modifires : Optional[List[Modify]] = None


class Catagories(BaseModel):
    catagory : Optional[str] =  None
    items : List[Item]

class Resturant(BaseModel):
    name : str 
    cuisine : Optional[str] = None
    timezone : Optional[str] = None
    opning_hour : Optional[Opning] = None 
    rating : Optional[float] = 0 
    cordinates : Dict[str,Any]
    delivery_options : List[str]
    menu : List[Catagories]