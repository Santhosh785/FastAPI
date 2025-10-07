from fastapi import FastAPI
from models import product

app = FastAPI() 

@app.get("/")     
def greet():
    return {"message": "hello from WEBSERVER"}

products = [
    product(1,"Samsung","A Mobile Phone",333.99,4),
    product(1,"Apple","A Mobile Phone",8833.99,4),

]


@app.get("/products")
def getproducts():
    return products
