from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        data = request.get_json()
        return redirect(url_for('map', data=data))
    else:
        return "Index page"

@app.route('/map', methods=["GET"])
def map(data):
    return render_template('main.html', data=data)


if __name__ == "__main__":
    app.secret_key = "woobus"
    app.debug = True
    app.run(port=8000)
