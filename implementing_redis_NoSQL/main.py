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
    # Verifica primeiro se esta em caching
    cached_item = redis_client.get(f"item:{name}")
    if cached_item:
        print("Item retrieved from cache") # para mostrar que o redis esta realmente funcionando e que o dado foi pego em caching
        return json.loads(cached_item)

    # Se não estiver no cache, consulte o banco de dados
    item = await collection.find_one({"name": name})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # Serialize o item para armazenamento em cache
    serialized_item = serialize_item(item)

    # Resultado do caching
    redis_client.set(f"item:{name}", json.dumps(serialized_item))
    return serialized_item
