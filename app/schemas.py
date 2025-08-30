from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class UserDelete(BaseModel):
    user_id: int
    model_config = ConfigDict(from_attributes=True)

# login request
class UserLogin(BaseModel):
    email: EmailStr
    password: str

#token response
class Token(BaseModel):
    access_token: str
    tokey_type: str = "bearer"
    