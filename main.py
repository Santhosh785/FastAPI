from fastapi import FastAPI
from models import product

app = FastAPI() 

@app.get("/")     
def greet():
    return {"message": "hello from WEBSERVER"}

products = [
    product(id=1,name="Samsung",description="A Mobile Phone",price=333.99,quantity=4),
    product(id=2,name="Samsung",description="A Mobile Phone",price=333.99,quantity=4),
    product(id=3,name="Samsung",description="A Mobile Phone",price=333.99,quantity=4),

]

@app.get("/products")
def getproducts():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id ==id:
            return product
        return "Products not Found"
    
@app.post("/product")
def add_products(product:product):
    products.append(product)
    return product
