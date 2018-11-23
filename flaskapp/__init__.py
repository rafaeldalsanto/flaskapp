from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_filename='flask.cfg'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    from flaskapp.model_base import ModelBase
    db.init_app(app)
    db.Model = db.make_declarative_base(model=ModelBase, metadata=None)
    migrate.init_app(app, db)


def register_blueprints(app):
    from pedidos import pedidos_blueprint
    app.register_blueprint(pedidos_blueprint)
