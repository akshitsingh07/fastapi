from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data":{"name":"Akshit"}}

@app.get('/aboutus')
def about():
    return {"data":{"page":"aboutus"}}

@app.get('/blog/{id}')
def blog(id):
    return {'data': id}

@app.get('/new/{id}')
def new(id: int):
    return {'data': id}