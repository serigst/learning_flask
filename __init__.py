from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")


@app.route('/login/')
def login():
    return render_template("login.html")


@app.route('/clickbait/')
def clickbait():
    return render_template("clickbait.html")


if __name__ == "__main__":
    app.run(debug=True)