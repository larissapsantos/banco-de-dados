from sys import prefix
from fastapi import APIRouter

auth = APIRouter(prefix="/autenticacao", tags=["auth"])

@auth.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return{"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}