from pydantic import BaseModel

class loginSchema(BaseModel):
    username: str 
    password: str 

class registerSchema(BaseModel):
    username: str 
    password: str
    email: str  