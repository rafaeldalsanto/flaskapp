from flask import request

from flaskapp.app import app


@app.route('/')
def index():
    x = request
    return 'Index Page'
