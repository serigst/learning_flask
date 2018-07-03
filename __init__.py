from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/posts/')
def posts():
    return render_template("posts.html")


@app.route('/login/')
def login():
    return render_template("login.html")


@app.route('/links/')
def links():
    return render_template("links.html")


if __name__ == "__main__":
    app.run(debug=True)
