from models.entities.processamento import Processamento
from services import scraping_service
from utils.dataset_util import DatasetUtil
from flask import jsonify


def find_processamento(tipo, ano):
    site_url = None
    tipo_descricao = None
    match tipo:
        case "viniferas":
            site_url = DatasetUtil.get_processamento_viniferas_dataset().get_site_url()
            tipo_descricao = (
                DatasetUtil.get_processamento_viniferas_dataset().get_sub_categoria()
            )
        case "americanas-e-hibridas":
            site_url = (
                DatasetUtil.get_processamento_americanas_e_hibridas_dataset().get_site_url()
            )
            tipo_descricao = (
                DatasetUtil.get_processamento_americanas_e_hibridas_dataset().get_sub_categoria()
            )
        case "uvas-de-mesa":
            site_url = (
                DatasetUtil.get_processamento_uvas_de_mesa_dataset().get_site_url()
            )
            tipo_descricao = (
                DatasetUtil.get_processamento_uvas_de_mesa_dataset().get_sub_categoria()
            )
        case "sem-classificacao":
            site_url = (
                DatasetUtil.get_processamento_sem_classificacao_dataset().get_site_url()
            )
            tipo_descricao = (
                DatasetUtil.get_processamento_sem_classificacao_dataset().get_sub_categoria()
            )

    # Executa a consulta por meio de Scraping, caso haja indisponibilidade do serviço, então
    # a consulta aos dados acontecerá a partir dos dados de histórico do Banco de Dados.
    data = scraping_service.scraping_processamento(site_url, tipo_descricao, ano)

    if data:
        return jsonify(data)
    else:
        tipo = "processamento-" + tipo
        query = Processamento.query
        response = (
            query.filter(Processamento.dataset_nome == tipo, Processamento.ano == ano)
            .order_by(Processamento.id)
            .all()
        )
        return jsonify([r.to_dict() for r in response])
