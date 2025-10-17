from datetime import datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    """Model for the response"""
    email: EmailStr
    name:str
    stack: str

class Profile(BaseModel):
    status: str
    user: User
    timestamp: datetime
    fact: str
