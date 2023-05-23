from fastapi import FastAPI

from pydantic import BaseModel,Field

import models
from database import engine , SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)



@app.get("/")

def root():
    return {"Dello": "world"}

@app.get("/login")

def login(): 
    return {"Page": "./"}
