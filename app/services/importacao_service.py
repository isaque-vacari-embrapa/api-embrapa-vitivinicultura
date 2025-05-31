from flask import jsonify
from models.entities.importacao import Importacao
from services import scraping_service
from utils.dataset_util import DatasetUtil


def find_importacao(tipo, ano):
    site_url = None
    tipo_descricao = None
    match tipo:
        case "vinhos-de-mesa":
            site_url = (
                DatasetUtil.get_importacao_vinhos_de_mesa_dataset().get_site_url()
            )
            tipo_descricao = (
                DatasetUtil.get_importacao_vinhos_de_mesa_dataset().get_sub_categoria()
            )
        case "espumantes":
            site_url = DatasetUtil.get_importacao_espumantes_dataset().get_site_url()
            tipo_descricao = (
                DatasetUtil.get_importacao_espumantes_dataset().get_sub_categoria()
            )
        case "uvas-frescas":
            site_url = DatasetUtil.get_importacao_uvas_frescas_dataset().get_site_url()
            tipo_descricao = (
                DatasetUtil.get_importacao_uvas_frescas_dataset().get_sub_categoria()
            )
        case "uvas-passas":
            site_url = DatasetUtil.get_importacao_uvas_passas_dataset().get_site_url()
            tipo_descricao = (
                DatasetUtil.get_importacao_uvas_passas_dataset().get_sub_categoria()
            )
        case "suco-de-uva":
            site_url = DatasetUtil.get_importacao_suco_de_uva_dataset().get_site_url()
            tipo_descricao = (
                DatasetUtil.get_importacao_suco_de_uva_dataset().get_sub_categoria()
            )

    # Executa a consulta por meio de Scraping, caso haja indisponibilidade do serviço, então
    # a consulta aos dados acontecerá a partir dos dados de histórico do Banco de Dados.
    data = scraping_service.scraping_importacao(site_url, tipo_descricao, ano)
    if data:
        return jsonify(data)
    else:
        tipo = "importacao-" + tipo
        query = Importacao.query
        response = (
            query.filter(Importacao.dataset_nome == tipo, Importacao.ano == ano)
            .order_by(Importacao.id)
            .all()
        )
        return jsonify([r.to_dict() for r in response])
