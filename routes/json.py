from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/json")
def json():
    return jsonify(
        {
            "firstname": "Ryan",
            "lastname": "Ray",
            "scores": [10, 30, 40],
            "active": True,
            "age": 30,
            "address": {"city": "London", "street": "221b baker street"},
        }
    )
