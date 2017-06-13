from flask import Flask, render_template

# by default the folder for templates
# is called templates
# to use other folder we have to config
app = Flask(__name__, template_folder = "myowntemplatefolder")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
