from flask import Flask, jsonify, request, render_template, redirect, url_for
import json

app = Flask(__name__)

data = {}

@app.route('/', methods=["GET","POST"])
def index():
    global data

    file = open('spantree.json')
    data = json.loads(file.read())
    print(data)

    return render_template('main.html', data=data)


if __name__ == "__main__":
    app.secret_key = "woobus"
    app.debug = True
    app.run(port=8000)
