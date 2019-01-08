import os

import pytest

from empresas.gateways import inserir_empresa
from flaskapp.app import create_app
from flaskapp.extensions import db as _db


@pytest.fixture(scope='session')
def app():
    app = create_app('flask_test.cfg')
    with app.app_context():
        yield app


@pytest.fixture(scope='session')
def config(app):
    return app.config


@pytest.fixture(scope='session')
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='session')
def db(config):
    def delete_test_db():
        test_db = config['TEST_DB']
        if os.path.exists(test_db):
            os.remove(test_db)

    delete_test_db()
    _db.create_all()

    yield _db

    delete_test_db()


@pytest.fixture()
def sqlalchemy_session(db):
    connection = db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)
    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture()
def empresa(sqlalchemy_session):
    return inserir_empresa(nome='Empresa')
