from flask import request, jsonify

from flaskapp import app, db
from flaskapp.models import Empresa


@app.route('/')
def index():
    empresas = Empresa.query.all()
    # empresa = Empresa(nome='Teste')
    # db.session.add(empresa)
    # db.session.commit()


    return jsonify([
        {
            'id': empresa.id,
            'nome': empresa.nome,
            'data_de_criacao': empresa.data_de_criacao,
            'ultima_alteracao': empresa.ultima_alteracao
        }
        for empresa in empresas
    ])
