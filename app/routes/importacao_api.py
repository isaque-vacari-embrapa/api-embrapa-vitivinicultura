from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from infrastructure.cache import cache
from infrastructure.config import Config
from services.importacao_service import find_importacao

importacao_api = Blueprint("importacao_api", __name__)


@importacao_api.route("/importacoes", methods=["GET"])
@jwt_required()
@cache.cached(query_string=True)
def get_importacao():
    """
    Retorna as importações de derivados de uva.
    Listagem de importações de derivados de uva por tipo e ano.
    ---
    operationId:
        Busca por tipo e ano de importação
    tags:
        - Banco de Dados de Vitivinicultura
    security:
        - bearerAuth: []
    parameters:
        - in: query
          name: tipo
          description: Tipo
          type: string
          default: vinhos-de-mesa
          required: true
          enum: [vinhos-de-mesa,espumantes,uvas-frescas,uvas-passas,suco-de-uva]
        - in: query
          name: ano
          description: Ano
          type: integer
          default: 2024
          required: true
          enum: [1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
    responses:
        200:
            description: Importação de derivados de uva
            schema:
                id: ImportacaoResponse
                properties:
                    tipo:
                        type: string
                        description: Tipo da uva
                    ano:
                        type: integer
                        description: Ano
                    pais:
                        type: string
                        description: País
                    quantidade:
                        type: integer
                        format: int32
                        description: Quantidade em Kg
                    valor:
                        type: integer
                        format: int32
                        description: Valor em US$
        400:
            description: Requisição inválida
            schema:
                id: ErrorResponse
                properties:
                    message:
                        type: string
                        description: Mensagem de erro
        401:
            description: Requisição não autorizada
            schema:
                id: ErrorResponse
                properties:
                    message:
                        type: string
                        description: Mensagem de erro
        500:
            description: Erro interno do servidor
            schema:
                id: ErrorResponse
                properties:
                    message:
                        type: string
                        description: Mensagem de erro
    """
    tipo = request.args.get("tipo")
    if not tipo or tipo not in [
        "vinhos-de-mesa",
        "espumantes",
        "uvas-frescas",
        "uvas-passas",
        "suco-de-uva",
    ]:
        mensagem_erro = "Tipo da uva não informado ou inválido, informe um tipo válido"
        return (
            jsonify({"message": mensagem_erro}),
            400,
        )

    ano = request.args.get("ano", type=int)
    if not ano or ano not in range(
        Config.MIN_ANO_IMPORTACAO, Config.MAX_ANO_IMPORTACAO + 1
    ):
        mensagem_erro = f"Ano não informado ou inválido, informe um ano entre {Config.MIN_ANO_IMPORTACAO} e {Config.MAX_ANO_IMPORTACAO}"
        return (
            jsonify({"message": mensagem_erro}),
            400,
        )

    return find_importacao(tipo, ano)
