from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/callname")
def create_name():
    return {"hello": "Saran_yeen"}


# create_name("Saran_yeen")

# @app.get("/test")
# def read_name():
#     return {"Hello": "World2"}


handler = Mangum(app)
