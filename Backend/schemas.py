from pydantic import BaseModel ,EmailStr,Field


    
class UserBase(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr

class User(UserBase):
    id: int