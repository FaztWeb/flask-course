from flask import Flask
from flask import request

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return "Hello World"

# the arguments: ?params1=1
@app.route('/params')
def params():
    parameter1 = request.args.get('params1', 'params no exists')
    parameter2 = request.args.get('params2', 'params no exists')
    return "the first paramter is : {} and the second is {}".format(parameter1, paramter2)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
