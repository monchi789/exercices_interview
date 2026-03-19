from pydantic import BaseModel

class User(BaseModel):
    id: str
    gender: str
    first_name: str
    last_name: str
    email: str
    age: int

