# Wasfi Momen
# TODO: Make sure comments are correct.
# https://github.com/BunsenMcDubbs/tslworkshop

'''
 To run this file you must have flask installed. Run python hello.py to execute.
'''
# import flask
from flask import Flask, send_from_directory

# Tells flask that the app variable will be the name of a function
app = Flask(__name__)

# set the app's directory route
# @app.route("/")

# set the app's directory route, you must type localhost/hello to access the function.
@app.route("/hello")
@app.route("/hello/<name>") # custom parameter name to take url parameter and custom input.

# Hello world. Lmao changed from previous commits.
def hello(name="Michelle"):
    return "Hello %s!" % name

# helloSecond() doesn't work, unless you add a route handler.
# def helloSecond(name = "World"):
#     return "Hello %s!" % name

@app.route("/")
@app.route("/<path:filepath>")
def index(filepath="index.html"): # another custom path in the url that will send index.html
    return send_from_directory("", filepath)





# tells python to tell flask name == main, main being the accepted way of telling this entire file should run (i think)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug = True) # Riyan and I looked this up, you can pass paramters here to tell what port and host to run on.
    # host = what host IP you want to run it on.
    # port = what port to connect to on the host.
    # debug = whether or not to set the server to debug mode. In debug mode, saving this file will restart the file.
