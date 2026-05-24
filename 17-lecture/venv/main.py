from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()


# Model
class Tea(BaseModel):
    id: int
    name: str
    origin: str


# List to store teas
teas: List[Tea] = []


# Root route
@app.get("/")
def read_root():
    return {"message": "welcome to chai or code"}


# Get all teas
@app.get("/teas")
def get_teas():
    return teas


# Add tea
@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea


# Update tea
@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):

    for index, tea in enumerate(teas):

        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea

    return {"error": "Tea not found"}


# Delete tea
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):

    for index, tea in enumerate(teas):

        if tea.id == tea_id:
            deleted_tea = teas.pop(index)
            return deleted_tea

    return {"error": "Tea not found"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)