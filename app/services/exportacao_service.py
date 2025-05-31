from flask import jsonify
from models.entities.exportacao import Exportacao
from services import scraping_service
from utils.dataset_util import DatasetUtil


def find_exportacao(tipo, ano):
    site_url = None
    tipo_descricao = None
    match tipo:
        case "vinhos-de-mesa":
            site_url = (
                DatasetUtil.get_exportacao_vinhos_de_mesa_dataset().get_site_url()
            )
            tipo_descricao = (
                DatasetUtil.get_exportacao_vinhos_de_mesa_dataset().get_sub_categoria()
            )
        case "espumantes":
            site_url = DatasetUtil.get_exportacao_espumantes_dataset().get_site_url()
            tipo_descricao = (
                DatasetUtil.get_exportacao_espumantes_dataset().get_sub_categoria()
            )
        case "uvas-frescas":
            site_url = DatasetUtil.get_exportacao_uvas_frescas_dataset().get_site_url()
            tipo_descricao = (
                DatasetUtil.get_exportacao_uvas_frescas_dataset().get_sub_categoria()
            )
        case "suco-de-uva":
            site_url = DatasetUtil.get_exportacao_suco_de_uva_dataset().get_site_url()
            tipo_descricao = (
                DatasetUtil.get_exportacao_suco_de_uva_dataset().get_sub_categoria()
            )

    # Executa a consulta por meio de Scraping, caso haja indisponibilidade do serviço, então
    # a consulta aos dados acontecerá a partir dos dados de histórico do Banco de Dados.
    data = scraping_service.scraping_exportacao(site_url, tipo_descricao, ano)
    if data:
        return jsonify(data)
    else:
        tipo = "exportacao-" + tipo
        query = Exportacao.query
        response = (
            query.filter(Exportacao.dataset_nome == tipo, Exportacao.ano == ano)
            .order_by(Exportacao.id)
            .all()
        )
        return jsonify([r.to_dict() for r in response])
