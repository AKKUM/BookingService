import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world, welcome to Booking Service!'