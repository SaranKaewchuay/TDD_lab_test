from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
nick = None

@app.get("/callname/{name}")
def read_name(name: str = None):
    global nick
    nick = name
    return {"hello": name}
  
    
@app.post("/callname")
def post_name():
    return {"hello": nick}

    


# create_name("Saran_yeen")

# @app.get("/test")
# def read_name():
#     return {"Hello": "World2"}


handler = Mangum(app)
