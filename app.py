from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return open("frontend/home.html", "r")