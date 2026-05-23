# Import FastAPI to create the API
from fastapi import FastAPI

# Import uvicorn to run the app
import uvicorn

# Create FastAPI app
app = FastAPI(
    title="My First API",
    description="A simple API using FastAPI",
    version="1.0.0"
)

# Home route
@app.get("/")
def read_root():
    return {"message": "main ! Welcome to FastAPI"}

# Dynamic route
@app.get("/main/{name}")
def read_item(name: str):
    return {"message": f"main, {name}!"}

# Run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)