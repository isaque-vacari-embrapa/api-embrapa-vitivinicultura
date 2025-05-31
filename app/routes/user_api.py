import bcrypt
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.base.database import db
from models.entities.user import User
from models.forms.user_form import UserForm
from models.forms.user_login_form import UserLoginForm

user_api = Blueprint("user_api", __name__)


@user_api.route("/register", methods=["POST"])
def user_register():
    """
    Registra um novo usuário.
    Registra um novo usuário, a partir do nome de usuário, senha e e-mail.
    ---
    operationId:
        Registra um novo usuário
    tags:
        - Usuário
    parameters:
        - in: body
          name: body
          required: true
          schema:
            id: UserRequest
            type: object
            properties:
                username:
                    type: string
                    description: Nome do usuário
                    required: true
                password:
                    type: string
                    description: Senha do usuário
                    required: true
                email:
                    type: string
                    description: E-mail do usuário
    responses:
        201:
            description: Usuário criado com sucesso
            schema:
                id: MessageResponse
                properties:
                    message:
                        type: string
                        description: Mensagem de resposta da requisição
        400:
            description: Requisição inválida
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
    try:
        data = request.get_json()
        user_form = UserForm(**data)
    except Exception:
        mensagem_erro = "Dados do usuário inválidos"
        return (
            jsonify({"message": mensagem_erro}),
            400,
        )
    else:
        if User.query.filter_by(username=user_form.username).first():
            mensagem_erro = "Usuário já existe"
            return (
                jsonify({"message": mensagem_erro}),
                400,
            )

        hashed_password = bcrypt.hashpw(
            str.encode(user_form.password), bcrypt.gensalt()
        )
        new_user = User(
            username=user_form.username,
            password=hashed_password,
            email=user_form.email,
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Usuário criado com sucesso"}), 201


@user_api.route("/login", methods=["POST"])
def login():
    """
    Faz login do usuário.
    Faz login do usuário e retorna um JSON Web Tokens (JWT) como token para acesso aos recursos da API.
    ---
    operationId:
        Faz o login do usuário
    tags:
        - Usuário
    parameters:
        - in: body
          name: body
          required: true
          schema:
            id: UserLogin
            type: object
            properties:
                username:
                    type: string
                    description: Nome do usuário
                    required: true
                password:
                    type: string
                    description: Senha do usuário
                    required: true
    responses:
        200:
            description: Login bem sucedido, retorna JWT (Access Token)
            schema:
                id: AccessToken
                properties:
                    access_token:
                        type: string
                        description: Access Token
        400:
            description: Requisição inválida
            schema:
                id: ErrorResponse
                properties:
                    message:
                        type: string
                        description: Mensagem de erro
        401:
            description: Usuário não autorizado
            schema:
                id: ErrorResponse
                properties:
                    message:
                        type: string
                        description: Mensagem de erro
    """
    try:
        data = request.get_json()
        user_login_form = UserLoginForm(**data)
    except Exception:
        mensagem_erro = "Credenciais inválidas"
        return (
            jsonify({"message": mensagem_erro}),
            400,
        )
    else:
        user = User.query.filter_by(username=user_login_form.username).first()
        if user:
            hashed_password = str.encode(data["password"])
            hashed_user_password = user.password
            if bcrypt.checkpw(hashed_password, hashed_user_password):
                # Converter o ID para String
                token = create_access_token(identity=str(user.id))
                return jsonify({"access_token": token}), 200
            else:
                mensagem_erro = "Usuário não autorizado, credenciais inválidas"
                return jsonify({"message": mensagem_erro}), 401
        else:
            mensagem_erro = "Usuário não autorizado, credenciais inválidas"
            return jsonify({"message": mensagem_erro}), 401
