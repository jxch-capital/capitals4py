from fastapi import FastAPI
from capitals4py import container

capitals4py = FastAPI()
capitals4py.container = container
