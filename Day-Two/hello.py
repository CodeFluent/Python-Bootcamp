# Wasfi Momen
# TODO: Make sure comments are correct.
# https://github.com/BunsenMcDubbs/tslworkshop

'''
 To run this file you must have flask installed. Run python hello.py to execute.
'''
# import flask
from flask import Flask

# Tells flask that the app variable will be the name of a function
app = Flask(__name__)

# set the app's directory route
@app.route("/")

# Hello world. Lmao changed from previous commits.
def hello():
    return "Hello PantherHackers!"

# helloSecond() didn't work. Guess it can only take in one function.
# def helloSecond(name = "World"):
#     return "Hello %s!" % name

# tells python to tell flask name == main, main being the accepted way of telling this entire file should run (i think)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80) # Riyan and I looked this up, you can pass paramters here to tell what port and host to run on.
