from fastapi import FastAPI
from . import container

app = FastAPI()
app.container = container

