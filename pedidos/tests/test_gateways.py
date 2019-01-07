import pytest

from empresas.servicos import inserir_empresa
from flaskapp.app import create_app
from flaskapp.extensions import db
from pedidos.gateways import obter_numero_do_proximo_pedido, inserir_pedido


@pytest.fixture(scope='module')
def client():
    app = create_app('flask_test.cfg')
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield client
    ctx.pop()


@pytest.fixture(scope='module')
def init_db():
    db.create_all()
    yield db
    db.session.rollback()
    db.drop_all()


@pytest.fixture
def empresa(client, init_db):
    return inserir_empresa(nome='Empresa')


class TestObterNumeroDoProximoPedido:
    def test_filtra_a_empresa(self, empresa):
        outra_empresa = inserir_empresa(nome='Outra empresa')
        inserir_pedido(empresa_id=outra_empresa['id'], numero=2)

        numero = obter_numero_do_proximo_pedido(empresa['id'])

        assert 1 == numero

    def test_retorna_um_quando_nao_ha_pedidos(self, empresa):
        numero = obter_numero_do_proximo_pedido(empresa['id'])

        assert 1 == numero
