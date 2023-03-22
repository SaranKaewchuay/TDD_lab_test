from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": {name}}

@app.post("/callname")
def read_name(name: str = None):
    return {"hello": {name}}


# @app.get("/test")
# def read_name():
#     return {"Hello": "World2"}


handler = Mangum(app)
