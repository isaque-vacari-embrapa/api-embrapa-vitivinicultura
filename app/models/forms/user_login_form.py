from pydantic import BaseModel


# Definindo o modelo de validação de login de usuário com Pydantic
class UserLoginForm(BaseModel):
    username: str
    password: str
