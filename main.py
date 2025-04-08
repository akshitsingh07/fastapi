from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data":{"name":"Akshit"}}

@app.get('.aboutus')
def about():
    return {"data":{"page":"aboutus"}}