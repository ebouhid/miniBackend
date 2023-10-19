from fastapi import FastAPI

app = FastAPI()

listaPets = []

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/pets")
def list_pets():
    return listaPets

@app.get("/pets/add")
def create_pet():
    listaPets.append({
    "name": "Jobson",
    "age": 2
})
