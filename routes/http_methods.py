from flask import Flask

app = Flask(__name__)

# by default all routes use GET method
@app.route("/")
def index():
    return "<h1>Hello World</h1>"


# most used HTTP Methods
# GET, POST, PUT, DELETE


# GET method
@app.route("/products", methods=["GET"])
def get_products():
    return "this should return a list of products"


# POST method
@app.route("/products", methods=["POST"])
def create_product():
    return "this should save a new product"


# PUT method
@app.route("/products", methods=["PUT"])
def update_product():
    return "this should updated product"


# DELETE method
@app.route("/products", methods=["DELETE"])
def delete_product():
    return "this should delete products"


# Multiples HTTP methods
@app.route("/test", methods=["GET", "POST"])
def get_and_create():
    return "this should work with GET and POST of products"
