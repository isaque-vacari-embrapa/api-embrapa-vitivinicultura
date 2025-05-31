from pydantic import BaseModel, EmailStr


# Definindo o modelo de validação de registro de usuário com Pydantic
class UserForm(BaseModel):
    username: str
    password: str
    email: EmailStr
