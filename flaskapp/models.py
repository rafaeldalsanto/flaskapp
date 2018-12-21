from flaskapp.database import Model
from flaskapp.extensions import db


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
