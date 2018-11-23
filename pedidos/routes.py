# from flask.json import jsonify

# from pedidos.models import Empresa
from . import pedidos_blueprint


@pedidos_blueprint.route('/')
def index():
    from pedidos.gateways import inserir_pedido
    pedido = inserir_pedido(empresa_id=1, numero=21)

    return 'ok'
    # empresas = Empresa.query.all()
    # # empresa = Empresa(nome='Teste')
    # # db.session.add(empresa)
    # # db.session.commit()
    #
    # return jsonify([
    #     {
    #         'id': empresa.id,
    #         'nome': empresa.nome,
    #         'data_de_criacao': empresa.data_de_criacao,
    #         'ultima_alteracao': empresa.ultima_alteracao
    #     }
    #     for empresa in empresas
    # ])
