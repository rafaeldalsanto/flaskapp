from flask import Flask

from flaskapp.extensions import db, migrate
from flaskapp.json_encoder import MyJSONEncoder


def create_app(config_filename='flask.cfg'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    app.json_encoder = MyJSONEncoder
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from geral import geral_blueprint
    from empresas import empresas_blueprint
    from pedidos import pedidos_blueprint

    app.register_blueprint(geral_blueprint)
    app.register_blueprint(empresas_blueprint)
    app.register_blueprint(pedidos_blueprint)
