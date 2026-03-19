from pydantic import BaseModel,EmailStr

class User(BaseModel):
    user_id: int
    username : str
    email : EmailStr 

data = {
    'user_id': '10',
    'username': 'Meet',
    'email': 'adc@gmail.com'
}

user = User(**data)
print(user)

