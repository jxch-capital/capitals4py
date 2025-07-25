from capitals4py.api import router


@router.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}
