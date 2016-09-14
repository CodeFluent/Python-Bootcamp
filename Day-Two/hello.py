# https://github.com/BunsenMcDubbs/tslworkshop

from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello FUCKERS!"
# def helloSecond(name = "World"):
#     return "Hello %s!" % name


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
