# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import collection, redis_client
from bson import ObjectId
import json

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

# Função para converter o item do MongoDB em um dicionário serializável
def serialize_item(item):
    item['_id'] = str(item['_id'])  # Converte ObjectId para string
    return item

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    new_item = await collection.insert_one(item.dict())
    created_item = await collection.find_one({"_id": new_item.inserted_id})
    return serialize_item(created_item)

@app.get("/items/{name}", response_model=Item)
async def read_item(name: str):
    # Check cache first
    cached_item = redis_client.get(f"item:{name}")
    if cached_item:
        print("Item retrieved from cache")
        return json.loads(cached_item)

    # If not in cache, query the database
    item = await collection.find_one({"name": name})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # Serialize the item for caching
    serialized_item = serialize_item(item)

    # Cache the result
    redis_client.set(f"item:{name}", json.dumps(serialized_item))
    return serialized_item
