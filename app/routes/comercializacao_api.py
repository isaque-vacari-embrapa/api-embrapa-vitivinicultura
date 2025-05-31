from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from infrastructure.cache import cache
from infrastructure.config import Config
from services.comercializacao_service import find_comercializacao

comercializacao_api = Blueprint("comercializacao_api", __name__)


@comercializacao_api.route("/comercializacoes", methods=["GET"])
@jwt_required()
@cache.cached(query_string=True)
def get_comercializacao():
    """
    Retorna a comercialização em L. de vinhos e derivados no Rio Grande do Sul/RS.
    Listagem da comercialização em L. de vinhos e derivados no Rio Grande do Sul/RS por ano.
    ---
    operationId:
        Busca por ano de comercialização
    tags:
        - Banco de Dados de Vitivinicultura
    security:
        - bearerAuth: []
    parameters:
        - in: query
          name: ano
          description: Ano
          type: integer
          default: 2023
          required: true
          enum: [1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
    responses:
        200:
            description: Dados da comercialização em L. de vinhos e derivados no Rio Grande do Sul/RS
            schema:
                id: ComercializacaoResponse
                properties:
                    ano:
                        type: integer
                        description: Ano
                    produto:
                        type: string
                        description: Produto
                    quantidade:
                        type: integer
                        format: int32
                        description: Quantidade em L.
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
    ano = request.args.get("ano", type=int)
    if not ano or ano not in range(Config.MIN_ANO, Config.MAX_ANO + 1):
        mensagem_erro = f"Ano não informado ou inválido, informe um ano entre {Config.MIN_ANO} e {Config.MAX_ANO}"
        return (
            jsonify({"message": mensagem_erro}),
            400,
        )

    return find_comercializacao(ano)
