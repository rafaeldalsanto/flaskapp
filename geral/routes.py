from flask import render_template

from geral import geral_blueprint


@geral_blueprint.route('/')
def index():
    return render_template('index.html')
