from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field
from capitalcom.client_demo import *

from config import *

cl = Client(login, password, API_KEY)

app = FastAPI(
    title='Trading App'
)

fake_trades = []

users = [
    {'id': 1, 'name': 'Anton', 'age':  24},
    {'id': 2, 'name': 'Tunga', 'age':  24},
    {'id': 3, 'name': 'Pavel', 'age':  25},
    {'id': 4, 'name': 'Sergei', 'age': 37},
]

class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float

class User(BaseModel):
    id: int
    name: str
    age: int

@app.get('/user/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in users if user.get('id') == user_id]

@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status code': 200, 'data': fake_trades}, 