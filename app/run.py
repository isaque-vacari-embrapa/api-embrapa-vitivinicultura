import logging

from flasgger import Swagger
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from infrastructure.cache import cache
from infrastructure.config import Config
from models.base.database import db
from routes.comercializacao_api import comercializacao_api
from routes.exportacao_api import exportacao_api
from routes.importacao_api import importacao_api
from routes.processamento_api import processamento_api
from routes.producao_api import producao_api
from routes.user_api import user_api

logger = logging.getLogger("app-api")

app = Flask(__name__)
app.config.from_object(Config)
app.json.sort_keys = Config.JSON_SORT_KEYS
app.register_blueprint(comercializacao_api)
app.register_blueprint(exportacao_api)
app.register_blueprint(importacao_api)
app.register_blueprint(processamento_api)
app.register_blueprint(producao_api)
app.register_blueprint(user_api)

db.init_app(app)
jwt = JWTManager(app)
cache.init_app(app)
swagger = Swagger(app)


@app.errorhandler(Exception)
def handle_generic_exception(e):
    mensagem_erro = None
    status_code = 500

    if hasattr(e, "code"):
        status_code = e.code

    match status_code:
        case 401:
            mensagem_erro = "Access token ausente ou inválido"
        case 404:
            mensagem_erro = "Recurso não encontrado"
        case 405:
            mensagem_erro = "Método não permitido"
        case 422:
            mensagem_erro = "Requisição inválida"
        case _:
            logger.error(e)
            mensagem_erro = "Um erro inesperado ocorreu, tente mais tarde"
    return (
        jsonify({"message": mensagem_erro}),
        status_code,
    )


@app.errorhandler(401)
def unauthorized(e):
    return unauthorized_response()


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return unauthorized_response()


@jwt.invalid_token_loader
def invalid_token_callback(callback):
    return unauthorized_response()


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return unauthorized_response()


def unauthorized_response():
    mensagem_erro = "Access token ausente ou inválido"
    return (
        jsonify({"message": mensagem_erro}),
        401,
    )


def main():
    with app.app_context():
        logger.info("Inicializando aplicação")
        cache.clear()
        db.create_all(bind_key="auth")
    app.run(debug=True, host="0.0.0.0", port=Config.DEFAULT_PORT)


if __name__ == "__main__":
    main()
