from fastapi import FastAPI
from pydantic import BaseModel
from deletebyname import del_by_name

app = FastAPI()

petList = []

class Pet(BaseModel):
    name: str
    age: int


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/pets")
def list_pets():
    return petList

@app.post("/pets/add")
def create_pet(pet: Pet):
    petList.append({
    "name": pet.name,
    "age": pet.age
})

@app.delete("/pets/delete")
def delete(name: str):
    cleanList = del_by_name(name,petList)
    petList = cleanList
    return petList