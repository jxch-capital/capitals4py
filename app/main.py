from fastapi import FastAPI
from app import container

app = FastAPI()
app.container = container
