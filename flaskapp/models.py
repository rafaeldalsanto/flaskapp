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


class Empresa(Model):
    nome = db.Column(db.String(length=200))


class Cliente(Model):
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    nome = db.Column(db.String(length=200))

    empresa = db.relationship('Empresa')


class Produto(Model):
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    nome = db.Column(db.String(length=200))

    empresa = db.relationship('Empresa')


class Pedido(Model):
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=True)
    numero = db.Column(db.Integer)
    data_de_emissao = db.Column(db.DateTime)
    total = db.Column(db.Numeric(precision=21, scale=6))

    empresa = db.relationship('Empresa')
    cliente = db.relationship('Cliente')
    itens = db.relationship('ItemDoPedido', back_populates='pedido')


class ItemDoPedido(Model):
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    preco_de_tabela = db.Column(db.Numeric(precision=21, scale=6))
    preco_liquido = db.Column(db.Numeric(precision=21, scale=6))
    quantidade = db.Column(db.Numeric(precision=21, scale=6))
    total = db.Column(db.Numeric(precision=21, scale=6))

    empresa = db.relationship('Empresa')
    pedido = db.relationship('Pedido', back_populates='itens')
    produto = db.relationship('Produto')
