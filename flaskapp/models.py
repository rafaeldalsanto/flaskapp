from flaskapp import db


class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(length=200))


class Cliente(db.Model):
    empresa = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    nome = db.Column(db.String(length=200))


class Produto(db.Model):
    empresa = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    nome = db.Column(db.String(length=200))


class Pedido(db.Model):
    empresa = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=True)
    numero = db.Column(db.Integer)
    data_de_emissao = db.Column(db.DateTime)
    total = db.Column(db.Numeric(precision=21, scale=6))


class ItemDoPedido(db.Model):
    empresa = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    produto = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    preco_de_tabela = db.Column(db.Numeric(precision=21, scale=6))
    preco_liquido = db.Column(db.Numeric(precision=21, scale=6))
    quantidade = db.Column(db.Numeric(precision=21, scale=6))
    total = db.Column(db.Numeric(precision=21, scale=6))
