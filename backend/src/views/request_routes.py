from unittest import result
from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.plano_aula import PlanoAula
from ..models.emprestimo import Emprestimo
from ..models.solicitacao import Solicitacao
from ..repositories.plano_aula import PlanoAulaRepos
from ..repositories.emprestimo import EmprestimoRepos
from ..repositories.solicitacao import SolicitacaoRepos

request = APIRouter(prefix="/requisicao", tags=["request"])



### CRUD - PLANOS DE AULA ###

@request.get("/")
async def requisicao():
    """
    Essa é a rota padrão de requisição do sistema. Todas as rotas de requisição precisam de autenticação
    """
    return{"mensagem": "Você acessou a rota padrão de requisicao"}

@request.get("/planos-de-aula")
async def listar_planos(db: Session = Depends(get_db)):
    """
    Essa é a rota para listar todos os planos de aula cadastrados no sistema
    """
    repo = PlanoAulaRepos()
    result = repo.listar(db)
    if (not result):
        return {"Não foram encontrados planos de aula cadastrados"}
    
    dados = []
    for plano in result:
        dados.append({
            "id": plano.id,
            "titulo": plano.titulo,
            "descricao": plano.descricao,
            "status": plano.status,
            "id_professor": plano.id_professor,
            "id_coordenador": plano.id_coordenador
        })
    return dados

@request.get("/planos-de-aula/{id}")
async def obter_plano(id: int, db: Session = Depends(get_db)):
    """
    Essa é a rota para obter um plano de aula cadastrado no sistema, identificado pelo id
    """
    repo = PlanoAulaRepos()
    result = repo.buscar_por_id(db, id)
    if (result is None):
        return {"Plano de aula não encontrado"}
    dados = {
        "id": result.id,
        "titulo": result.titulo,
        "descricao": result.descricao,
        "status": result.status,
        "id_professor": result.id_professor,
        "id_coordenador": result.id_coordenador
    }
    return {"Plano de aula" : dados}

@request.post("/planos-de-aula")
async def criar_plano(
    titulo: str,           
    descricao: str,         
    status: str,           
    id_professor: int,     
    id_coordenador: int,   
    db: Session = Depends(get_db)
):
    """
    Essa é a rota para criar um plano de aula
    """
    repo = PlanoAulaRepos()
    novo_plano = PlanoAula(
        titulo=titulo,
        descricao=descricao,
        status=status,
        id_professor=id_professor,
        id_coordenador=id_coordenador
    )
    criado = repo.criar(db, novo_plano)
    return {
        "mensagem": "Plano de aula criado com sucesso!",
        "id": criado.id
    }

@request.put("/planos-de-aula/{id}")
async def atualizar_plano(
    id: int,
    titulo: str = Body(None),
    descricao: str = Body(None),
    status: str = Body(None),
    id_professor: int = Body(None),
    id_coordenador: int = Body(None),
    db: Session = Depends(get_db)
):
    """
    Atualiza plano de aula, sendo cada campo é um parâmetro opcional no body
    """
    repo = PlanoAulaRepos()
    plano = repo.buscar_por_id(db, id)
    if not plano:
        return {"erro": "Plano de aula não encontrado"}
    dados = {}
    if titulo is not None:
        dados["titulo"] = titulo
    if descricao is not None:
        dados["descricao"] = descricao
    if status is not None:
        dados["status"] = status
    if id_professor is not None:
        dados["id_professor"] = id_professor
    if id_coordenador is not None:
        dados["id_coordenador"] = id_coordenador
    if not dados:
        return {"erro": "Nenhum dado enviado para atualização"}
    atualizado = repo.editar(db, id, dados)
    return {
        "mensagem": "Plano de aula atualizado com sucesso!",
        "plano": {
            "id": atualizado.id,
            "titulo": atualizado.titulo,
            "descricao": atualizado.descricao,
            "status": atualizado.status,
            "id_professor": atualizado.id_professor,
            "id_coordenador": atualizado.id_coordenador
        }
    }
    
@request.delete("/planos-de-aula/{id}")
async def remover_plano(id: int, db: Session = Depends(get_db)):
    """
    Essa é a rota para deletar um plano de aula cadastrado no sistema, identificado pelo id
    """
    repo = PlanoAulaRepos()
    result = repo.deletar(db, id)
    if (result is None):
        return {"Plano de aula não encontrado"}
    return{"Plano de aula deletado com sucesso!"}



### CRUD - EMPRÉSTIMOS ###

@request.get("/emprestimos")
async def listar_emprestimos(db: Session = Depends(get_db)):
    """
    Essa é a rota para listar todos os empréstimos cadastrados no sistema
    """
    repo = EmprestimoRepos()
    result = repo.listar(db)
    if (not result):
        return {"Não foram encontrados empréstimos cadastrados"}
    
    dados = []
    for emprestimo in result:
        dados.append({
            "id": emprestimo.id,
            "quantidade": emprestimo.quantidade,
            "data_hora": emprestimo.data_hora,
            "id_escola": emprestimo.id_escola,
            "id_equipamento": emprestimo.id_equipamento,
            "id_plano_aula": emprestimo.id_plano_aula
        })
    return dados

# @request.get("/emprestimos/{emprestimo_id}")
# async def obter_emprestimo(emprestimo_id: int):

# @request.post("/emprestimos")
# async def criar_emprestimo(dados):

# @request.post("/emprestimos/{emprestimo_id}")
# async def atualizar_emprestimo(emprestimo_id: int, dados):

# @request.post("/emprestimos/{emprestimo_id}")
# async def remover_emprestimo(emprestimo_id: int):

# @request.post("/emprestimos/{emprestimo_id}/avaliacao")
# async def avaliar_emprestimo(emprestimo_id: int, status):



### CRUD - SOLICITAÇÕES ###

@request.get("/solicitacoes")
async def listar_solicitacoes(db: Session = Depends(get_db)):
    """
    Essa é a rota para listar todos os solicitações de aula cadastrados no sistema
    """
    repo = PlanoAulaRepos()
    result = repo.listar(db)
    if (not result):
        return {"Não foram encontrados solicitações cadastradas"}
    
    dados = []
    for solicitacao in result:
        dados.append({
            "id_administrador": solicitacao.id_administrador,
            "id_emprestimo": solicitacao.id_emprestimo,
            "id_coordenador": solicitacao.id_coordenador,
            "status": solicitacao.status
        })
    return dados

# @request.get("/solicitacoes/{solicitacoes_id}")
# async def obter_emprestimo(solicitacoes_id: int):

# @request.post("/solicitacoes")
# async def criar_emprestimo(dados):

# @request.post("/solicitacoes/{solicitacoes_id}")
# async def atualizar_emprestimo(solicitacoes_id: int, dados):

# @request.post("/solicitacoes/{solicitacoes_id}")
# async def remover_emprestimo(solicitacoes_id: int):

# @request.post("/solicitacoes/{solicitacoes_id}/avaliacao")
# async def avaliar_emprestimo(solicitacoes_id: int, status):



### TESTAS AS ROUTES:
# 1º source venv/bin/activate  
# 2º uvicorn src.main:app --reload