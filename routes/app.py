from flask import Flask
from flask import request

app = Flask(__name__)

# greets a nickname using a parameter
@app.route("/gretting/<nickname>")
def greeting(name):
    return "<h1>hello {}!</h1>".format(name)

# use a default value for parameter
@app.route("/",defaults={"name": "dude"})
@app.route("/<name>")
# @app.route("/<name>",defaults={"name": "dude"}) # this default value overrides the param
def home(name):
    return "<h1>Hello {}, you are on the home page!</h1>".format(name)

# you can pass methods and defaults
@app.route("/",methods=["GET", "POST"], defaults={"name": "dude"})
def options():
    return "test"

# By default the parameters are strings
# the parameters: /name
# the parameters: /name/1
@app.route("/params/")
@app.route("/params/<name>")
@app.route("/params/<name>/<lastName>")
def params(name="default name", lastName="default lastName"):
    return "the fullName is {} {}".format(name, lastName)

# you can pas a diferent datatype in the param
@app.route("/concat/<string:n1>/<string:n2>")
def contact(n1, n2):
    return n1 + n2

@app.route("/add/<int:n1>/<int:n2>")
def add(n1, n2):
    return str(n1 + n2)

# use string and int
@app.route("/user")
@app.route("/user/<name>")
@app.route("/user/<string:name>/<int:id>")
def user(name="default user", id=0):
    return "the user: {} has the id: {}".format(name, id)

# querys: the arguments: ?params1=1
@app.route("/params")
def params_querys():
    parameter1 = request.args.get("params1", "params no exists")
    parameter2 = request.args.get("params2", "params no exists")
    return "the first paramter is : {} and the second is {}".format(
            parameter1, paramter2
            )
