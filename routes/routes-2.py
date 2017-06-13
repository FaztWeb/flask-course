from flask import Flask
from flask import request

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return "Hello World"

# By default the parameters are strings
# the parameters: /name
# the parameters: /name/1
@app.route('/params/')
@app.route('/params/<name>')
@app.route('/params/<name>/<lastName>')
def params(name = "default name", lastName = "default lastName"):
    return "the fullName is {} {}".format(name, lastName)

# but if we need a numeric value
# we can use types on parameters
@app.route('/user')
@app.route('/user/<name>')
@app.route('/user/<string:name>/<int:id>')
def user(name = "default user", id = 0):
    return "the user: {} has the id: {}".format(name, id)

# To run the application
if __name__ == '__main__':
    app.run(port=8000, debug=True)
