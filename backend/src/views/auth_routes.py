from sys import prefix
from fastapi import APIRouter

auth = APIRouter(prefix="/autenticacao", tags=["auth"])

@auth.post("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do sistema. Nela, o usuário vai selecionar se é professor, coordenador ou administrador
    """
    return{"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}

@auth.post("/autenticar/administrador")
async def login_administrador(dados: dict):
    """
    Essa é a rota para acessar a tela de login de Administrador
    """
    matricula = dados["matricula"]
    return {"mensagem": "Cadastro encontrado"}

@auth.post("/autenticar/coordenador")
async def login_coordenador(dados: dict):
    """
    Essa é a rota para acessar a tela de login de Coordenador
    """
    rmatricula = dados["matricula"]
    senha = dados["senha"]
    return {"mensagem": "Cadastro encontrado"}

@auth.post("/autenticar/professor")
async def login_professor(dados: dict):
    """
    Essa é a rota para acessar a tela de login de Professor
    """
    rmatricula = dados["matricula"]
    senha = dados["senha"]
    return {"mensagem": "Cadastro encontrado"}