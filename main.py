from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Cloud-Native Serverless API",
    description="A lightweight REST API designed for cloud deployment.",
    version="1.0.0"
)

# Örnek veri modeli
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# Geçici bellek içi veritabanı (In-memory DB)
db = {}

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Welcome to the Cloud-Native REST API",
        "docs": "/docs"
    }

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "data": db[item_id]}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[item_id] = item
    return {"message": "Item successfully created", "item_id": item_id, "data": item}