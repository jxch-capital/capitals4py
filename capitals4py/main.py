from fastapi import FastAPI
from capitals4py import container
from capitals4py.api import router

app = FastAPI()
app.container = container
app.include_router(router)
