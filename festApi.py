# main.py 

from fastapi import FastAPI, status
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///all.db")
base = declarative_base()

app = FastAPI()

@app.get("/")
async def root():
    return "Olá mundo!"

@app.post("/all", status_code=status.HTTP_201_CREATED)
def create_all():
    return "Create all"

@app.get("/all/{id}")
def read_all():
    return "read item with id"

@app.put("/all/{id}")
def update(id:int):
    return "update of item"

@app.delete("/all/{id}")
def delete(id:int):
    return "delete item id"

@app.get("/all")
def readList(id: int):
    return "read list"