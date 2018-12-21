from sqlalchemy.ext.declarative import declared_attr

from flaskapp.extensions import db


class Model(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    data_de_criacao = db.Column(db.DateTime, nullable=False)
    ultima_alteracao = db.Column(db.DateTime, nullable=False)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self):
        return f'{self.__tablename__}(id={self.id})'
