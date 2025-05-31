from models.entities.producao import Producao
from services import scraping_service
from utils.dataset_util import DatasetUtil
from flask import jsonify


def find_producao(ano):
    # Executa a consulta por meio de Scraping, caso haja indisponibilidade do serviço, então
    # a consulta aos dados acontecerá a partir dos dados de histórico do Banco de Dados.
    data = scraping_service.scraping_producao(
        DatasetUtil.get_producao_dataset().get_site_url(), ano
    )

    if data:
        return jsonify(data)
    else:
        tipo = "producao"
        query = Producao.query
        response = (
            query.filter(Producao.dataset_nome == tipo, Producao.ano == ano)
            .order_by(Producao.id)
            .all()
        )
        return jsonify([r.to_dict() for r in response])
