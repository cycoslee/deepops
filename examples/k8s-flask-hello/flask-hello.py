#!/usr/bin/env python

from flask import Flask
from socket import gethostname

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from {}".format(gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0")
