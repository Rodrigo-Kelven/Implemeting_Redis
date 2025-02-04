# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Item as DBItem, redis_client
from pydantic import BaseModel
import json

app = FastAPI()

# Pydantic model
class ItemCreate(BaseModel):
    name: str
    description: str

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=ItemCreate)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = DBItem(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{name}", response_model=ItemCreate)
def read_item(name: str, db: Session = Depends(get_db)):
    # Check cache first
    cached_item = redis_client.get(f"item:{name}")
    if cached_item:
        print("Item retrieved from cache")
        return ItemCreate.parse_raw(cached_item.decode('utf-8'))

    # If not in cache, query the database
    item = db.query(DBItem).filter(DBItem.name == name).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # Convert the SQLAlchemy item to a Pydantic model
    item_data = ItemCreate(name=item.name, description=item.description)

    # Cache the result
    redis_client.set(f"item:{name}", item_data.json())
    return item_data
