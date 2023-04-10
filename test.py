from typing import List
from fastapi import FastAPI, Response, Path
from fastapi.responses import FileResponse
from pydantic.fields import Field
from pydantic.main import BaseModel

app = FastAPI()


class Trade(BaseModel):
    name: str 
    surname: str
    age: int = Field(gt=18, lt=100, title='Age')
    
users = [
    {'name': 'Anton', 'Surname': 'Zyanouchik', 'age': 25},
    ]

@app.post('/users')
def add_user(user: List[Trade]):
    users.extend(user)
    return {'data': users}
