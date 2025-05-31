import os

from dotenv import load_dotenv

load_dotenv()


# Configurações da Aplicação
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///vitivinicultura.db"
    SQLALCHEMY_BINDS = {"auth": "sqlite:///auth.db"}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JSON_SORT_KEYS = False
    DEFAULT_PORT = os.getenv("DEFAULT_PORT")
    MIN_ANO = 1970
    MAX_ANO = 2023
    MIN_ANO_IMPORTACAO = 1970
    MAX_ANO_IMPORTACAO = 2024
    MIN_ANO_EXPORTACAO = 1970
    MAX_ANO_EXPORTACAO = 2024
    SCRAPING_TIMEOUT_IN_SECONDS = 5
    SWAGGER = {
        "title": "Vitivinicultura",
        "uiversion": 3,
        "description": "API de consulta ao Banco de Dados de Vitivinicultura (uva, vinho e derivados) da Embrapa Uva e Vinho, disponível em: http://vitibrasil.cnpuv.embrapa.br.",
        "version": "v1",
        "termsOfService": "http://vitibrasil.cnpuv.embrapa.br/",
        "ui_params": {
            "apisSorter": "alpha",
            "operationsSorter": "alpha",
            "tagsSorter": "alpha",
        },
        "securityDefinitions": {
            "bearerAuth": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "scheme": "bearer",
                "description": 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"',
            }
        },
    }
