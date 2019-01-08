from empresas.gateways import inserir_empresa
from pedidos.gateways import obter_numero_do_proximo_pedido, inserir_pedido


class TestObterNumeroDoProximoPedido:
    def test_retorna_o_numero_do_proximo_pedido(self, empresa):
        inserir_pedido(empresa_id=empresa['id'], numero=2)

        numero = obter_numero_do_proximo_pedido(empresa['id'])

        assert 3 == numero

    def test_filtra_a_empresa(self, empresa):
        outra_empresa = inserir_empresa(nome='Outra empresa')
        inserir_pedido(empresa_id=outra_empresa['id'], numero=2)

        numero = obter_numero_do_proximo_pedido(empresa['id'])

        assert 1 == numero

    def test_retorna_um_quando_nao_ha_pedidos(self, empresa):
        numero = obter_numero_do_proximo_pedido(empresa['id'])

        assert 1 == numero
