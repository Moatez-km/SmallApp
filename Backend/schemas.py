from pydantic import BaseModel ,EmailStr


    
class UserBase(BaseModel):
    name: str
    email: str

class User(UserBase):
    id: int