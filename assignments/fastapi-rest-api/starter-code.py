# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example data model
class Book(BaseModel):
    id: int
    title: str
    author: str

# In-memory storage
books: List[Book] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# Add more endpoints for CRUD operations below
