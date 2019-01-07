from flaskapp.gateway_generico import inserir, atualizar, obter, obter_um
from flaskapp.models import Empresa


def inserir_empresa(**campos):
    return inserir(Empresa, **campos)


def atualizar_empresa(empresa_id, **campos):
    atualizar(Empresa, empresa_id, **campos)


def obter_empresas(**filtros):
    return obter(Empresa, **filtros)


def obter_uma_empresa(**filtros):
    return obter_um(Empresa, **filtros)
