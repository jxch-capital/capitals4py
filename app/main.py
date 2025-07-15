from fastapi import FastAPI
from app.containers import Container

app = FastAPI()
container = Container()
app.container = container

