from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


app = FastAPI()

items = []

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/")
async def read_items():
    return items

