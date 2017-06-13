from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name="Fazt"):
    age = 20
    myNumberList = [1, 2, 3, 4, 5]
    return render_template(
        'user.html',
        name = name,
        age = age,
        list = myNumberList
        )

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
