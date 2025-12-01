from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..repositories.administrador import AdministradorRepo
from ..repositories.coordenador import CoordenadorRepos
from ..repositories.professor import ProfessorRepos
from ..repositories.escola import EscolaRepos

auth = APIRouter(prefix="/autenticacao", tags=["auth"])

@auth.post("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do sistema. Nela, o usuário vai selecionar se é professor, coordenador ou administrador
    """
    return{"mensagem": "Você acessou a rota padrão de autenticação"}

@auth.post("/autenticar/administrador")
async def login_administrador(matricula: int, db: Session = Depends(get_db)):
    """
    Essa é a rota para a matrícula de Administrador no banco de dados
    """
    repo = AdministradorRepo()
    result = repo.buscar_por_id(db, matricula)
    print("Resultado -> ", result)
    if (result is None):
        return {"Cadastro não encontrado"}
    dados = {
        "matricula": result.matricula,
        "nome": result.nome,
        "email": result.email,
        "bairro": result.bairro,
        "uf": result.uf
    }
    return {"Cadastro" : dados}

@auth.post("/autenticar/coordenador")
async def login_coordenador(matricula: int, db: Session = Depends(get_db)):
    """
    Essa é a rota para a matrícula de Coordenador no banco de dados
    """
    repo = CoordenadorRepos()
    result = repo.buscar_por_id(db, matricula)
    print("Resultado -> ", result)
    if (result is None):
        return {"Cadastro não encontrado"}
    dados = {
        "matricula": result.matricula,
        "nome": result.nome,
        "situacao": result.situacao,
        "id_escola": result.id_escola
    }
    if (dados.get("situacao") == "inativo"):
        return {"Usuário inativo"}
    return {"Cadastro" : dados}

@auth.post("/autenticar/professor")
async def login_professor(matricula: int, db: Session = Depends(get_db)):
    """
    Essa é a rota para a matrícula de Professor no banco de dados
    """
    repo = ProfessorRepos()
    result = repo.buscar_por_id(db, matricula)
    print("Resultado -> ", result)
    if (result is None):
        return {"Cadastro não encontrado"}
    dados = {
        "matricula": result.matricula,
        "nome": result.nome,
        "situacao": result.situacao,
        "id_escola": result.id_escola
    }
    if (dados.get("situacao") == "inativo"):
        return {"Usuário inativo"}
    return {"Cadastro" : dados}