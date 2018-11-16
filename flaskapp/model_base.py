from datetime import datetime

from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declared_attr


class ModelBase(Model):
    id = Column(Integer, primary_key=True, nullable=False)
    data_de_criacao = Column(DateTime, nullable=False, default=datetime.now)
    ultima_alteracao = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self):
        return f'{self.__tablename__}(id={self.id})'
