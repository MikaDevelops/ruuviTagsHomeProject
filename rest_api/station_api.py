from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/data/<datetimefrom>")
def data(datetimefrom):
    daatta = {"matti":"yskii"}
    return jsonify(daatta), 200

if __name__ == "__main__":
    app.run(debug=True)