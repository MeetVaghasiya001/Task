from pydantic import BaseModel
from typing import Optional,List
from datetime import time,datetime,date


class Layovers(BaseModel):
    location : Optional[str]
    durationInMinutes : Optional[int]
    duration : Optional[str]

class Ixigo(BaseModel):
    date : date
    name : Optional[str] = None 
    flight_from : Optional[str] = None 
    to : Optional[str] = None 
    flight_duration : Optional[str]
    flight_no : str = None
    price : int 
    departure_time : time 
    arrival_time : time 
    baggege : Optional[str] = None
    hand_baggege : Optional[str] = None
    offer : Optional[str] = None
    layover : Optional[List[Layovers]] = None
