from models.entities.comercializacao import Comercializacao
from services import scraping_service
from utils.dataset_util import DatasetUtil
from flask import jsonify


def find_comercializacao(ano):
    # Executa a consulta por meio de Scraping, caso haja indisponibilidade do serviço, então
    # a consulta aos dados acontecerá a partir dos dados de histórico do Banco de Dados.
    data = scraping_service.scraping_comercializacao(
        DatasetUtil.get_comercializacao_dataset().get_site_url(), ano
    )

    if data:
        return jsonify(data)
    else:
        tipo = "comercializacao"
        query = Comercializacao.query
        response = (
            query.filter(
                Comercializacao.dataset_nome == tipo, Comercializacao.ano == ano
            )
            .order_by(Comercializacao.id)
            .all()
        )
        return jsonify([r.to_dict() for r in response])
