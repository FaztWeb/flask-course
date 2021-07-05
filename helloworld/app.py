from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

if __name__== '__main__':
    #length of ports: 2**16
    app.run(debug = True, port = 8000)
