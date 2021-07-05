from flask import Flask
from flask import request

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return "Hello World"


if __name__ == '__main__':
    app.run(port=8000, debug=True)
