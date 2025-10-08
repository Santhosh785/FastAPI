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

@app.put("/product")
def update_products(id:int,product:product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return "Product added Successfully"
        
        return "No product Found"
    
@app.delete("/product")
def delete_products(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "Product Deleted"
        return "Products Not Found"