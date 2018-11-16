from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base(object):
    id = Column(Integer, primary_key=True, nullable=False)
    data_de_criacao = Column(DateTime, nullable=False)
    ultima_alteracao = Column(DateTime, nullable=False)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self):
        return f'{self.__tablename__}(id={self.id})'


class Empresa(Base):
    nome = Column(String(length=200))


class Cliente(Base):
    empresa = Column(Integer, ForeignKey('empresa.id'), nullable=False)
    nome = Column(String(length=200))


class Produto(Base):
    empresa = Column(Integer, ForeignKey('empresa.id'), nullable=False)
    nome = Column(String(length=200))


class Pedido(Base):
    empresa = Column(Integer, ForeignKey('empresa.id'), nullable=False)
    cliente = Column(Integer, ForeignKey('cliente.id'), nullable=True)
    numero = Column(Integer)
    data_de_emissao = Column(DateTime)
    total = Column(Numeric(precision=21, scale=6))


class ItemDoPedido(Base):
    empresa = Column(Integer, ForeignKey('empresa.id'), nullable=False)
    produto = Column(Integer, ForeignKey('produto.id'), nullable=False)
    preco_de_tabela = Column(Numeric(precision=21, scale=6))
    preco_liquido = Column(Numeric(precision=21, scale=6))
    quantidade = Column(Numeric(precision=21, scale=6))
    total = Column(Numeric(precision=21, scale=6))
