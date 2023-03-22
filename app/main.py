from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

Name = None

@app.get("/callname/{name}")
def read_name(name: str = None):
    global Name
    Name = name
    return {"hello": name}
  
    
@app.post("/callname")
def post_name():
    return {"hello": Name}

    
handler = Mangum(app)
