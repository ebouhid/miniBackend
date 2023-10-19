from fastapi import FastAPI

app = FastAPI()

listaPets = []

listaPets.append({
    "name": "Jobson",
    "age": 2
})

@app.get("/pets")
def list_pets():
    return listaPets