from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

listaPets = []

class Pet(BaseModel):
    name: str
    age: int


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/pets")
def list_pets():
    return listaPets

@app.post("/pets/add")
def create_pet(pet):
    listaPets.append({
    "name": pet.name,
    "age": pet.age
})
