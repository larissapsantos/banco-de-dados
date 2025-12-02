from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database import get_db
from src.models.plano_aula import PlanoAula
from src.repositories.plano_aula import PlanoAulaRepos
from src.repositories.coordenador import CoordenadorRepos
from src.repositories.administrador import AdministradorRepo
from pydantic import BaseModel

request = APIRouter(prefix="/requisicao", tags=["request"])

# --- MODELOS DE DADOS (Schemas) ---
class PlanoAulaSchema(BaseModel):
    titulo: str
    descricao: str
    status: str
    id_professor: int
    id_coordenador: int

class ConsolidacaoSchema(BaseModel):
    id_coordenador: int
    planos_ids: List[int]

class AprovarSchema(BaseModel):
    status: str

# --- ROTAS DE LEITURA (GET) ---

@request.get("/planos-de-aula")
async def listar_planos(db: Session = Depends(get_db)):
    """Busca todos os planos no banco de dados (Geral)"""
    repo = PlanoAulaRepos()
    planos = repo.listar(db)
    return planos

@request.get("/planos-de-aula/coordenador/{matricula}")
async def listar_planos_por_coordenador(matricula: int, db: Session = Depends(get_db)):
    """Lista planos de aula APENAS da escola deste coordenador."""
    repo_coord = CoordenadorRepos()
    coordenador = repo_coord.buscar_por_id(db, matricula)
    
    if not coordenador:
        raise HTTPException(status_code=404, detail="Coordenador não encontrado")
    
    repo_plano = PlanoAulaRepos()
    # O # type: ignore diz pro VS Code: "Eu sei que isso é um número, confia em mim"
    planos = repo_plano.listar_por_escola(db, coordenador.id_escola) # type: ignore
    return planos

@request.get("/planos-de-aula/administrador/{matricula}")
async def listar_planos_para_admin(matricula: int, db: Session = Depends(get_db)):
    """
    Rota Inteligente: Descobre o bairro do Admin e busca planos das escolas de lá.
    """
    repo_admin = AdministradorRepo()
    admin = repo_admin.buscar_por_id(db, matricula)
    
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador não encontrado")
    
    repo_plano = PlanoAulaRepos()
    # Busca apenas planos ENVIADOS que sejam do bairro desse admin
    # O # type: ignore evita o erro "Column[str] is not assignable to str"
    planos = repo_plano.listar_pendentes_por_bairro(db, admin.bairro) # type: ignore
    return planos

# --- ROTAS DE ESCRITA (POST/PUT/DELETE) ---

@request.post("/planos-de-aula")
async def criar_plano(dados: PlanoAulaSchema, db: Session = Depends(get_db)):
    """Professor cria um novo plano"""
    repo = PlanoAulaRepos()
    novo_plano = PlanoAula(
        titulo=dados.titulo,
        descricao=dados.descricao,
        status=dados.status,
        id_professor=dados.id_professor,
        id_coordenador=dados.id_coordenador
    )
    repo.criar(db, novo_plano)
    return {"mensagem": "Plano criado com sucesso!", "id": novo_plano.id}

@request.post("/planos-de-aula/consolidar")
async def consolidar_planos(dados: ConsolidacaoSchema, db: Session = Depends(get_db)):
    """Coordenador envia os planos para a administração"""
    repo = PlanoAulaRepos()
    for id_plano in dados.planos_ids:
        # Atualiza o status de cada plano selecionado
        plano = repo.editar(db, id_plano, {"status": "ENVIADO"})
        if not plano:
            print(f"Aviso: Plano {id_plano} não encontrado ao consolidar.")
            
    return {"mensagem": f"{len(dados.planos_ids)} planos enviados para a administração!"}

@request.put("/planos-de-aula/{id}/avaliacao")
async def avaliar_plano(id: int, dados: AprovarSchema, db: Session = Depends(get_db)):
    """Administrador aprova ou rejeita o plano"""
    repo = PlanoAulaRepos()
    
    # Atualiza o status
    atualizado = repo.editar(db, id, {"status": dados.status})
    
    if atualizado is None:
        raise HTTPException(status_code=404, detail="Plano não encontrado")

    return {"mensagem": f"Plano atualizado para {dados.status}!"}

@request.delete("/planos-de-aula/{id}")
async def deletar_plano(id: int, db: Session = Depends(get_db)):
    """Remove um plano pelo ID"""
    repo = PlanoAulaRepos()
    sucesso = repo.deletar(db, id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return {"mensagem": "Plano removido com sucesso"}

# --- OUTRAS ROTAS (Placeholders) ---

@request.get("/emprestimos")
async def listar_emprestimos():
    return {"mensagem": "Rota de empréstimos ainda não implementada."}

@request.get("/equipamentos")
async def listar_equipamentos():
    return {"mensagem": "Rota de equipamentos ainda não implementada."}

# ///////////////////////////////////////////////////////////////////////////
# //////////////// CÓDIGO ORIGINAL SEM AJUSTES //////////////////////////////
# ///////////////////////////////////////////////////////////////////////////

# from unittest import result
# from fastapi import APIRouter, Depends, Body
# from sqlalchemy.orm import Session
# from ..database import get_db
# from ..models.plano_aula import PlanoAula
# from ..models.emprestimo import Emprestimo
# from ..models.solicitacao import Solicitacao
# from ..repositories.plano_aula import PlanoAulaRepos
# from ..repositories.emprestimo import EmprestimoRepos
# from ..repositories.solicitacao import SolicitacaoRepos

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from src.database import get_db
# from src.models.plano_aula import PlanoAula
# from src.repositories.plano_aula import PlanoAulaRepos
# from pydantic import BaseModel

# request = APIRouter(prefix="/requisicao", tags=["request"])

# request = APIRouter(prefix="/requisicao", tags=["request"])



# ### CRUD - PLANOS DE AULA ###

# @request.get("/")
# async def requisicao():
#     """
#     Essa é a rota padrão de requisição do sistema. Todas as rotas de requisição precisam de autenticação
#     """
#     return{"mensagem": "Você acessou a rota padrão de requisicao"}

# @request.get("/planos-de-aula")
# async def listar_planos(db: Session = Depends(get_db)):
#     """
#     Essa é a rota para listar todos os planos de aula cadastrados no sistema
#     """
#     repo = PlanoAulaRepos()
#     result = repo.listar(db)
#     if (not result):
#         return {"Não foram encontrados planos de aula cadastrados"}
    
#     dados = []
#     for plano in result:
#         dados.append({
#             "id": plano.id,
#             "titulo": plano.titulo,
#             "descricao": plano.descricao,
#             "status": plano.status,
#             "id_professor": plano.id_professor,
#             "id_coordenador": plano.id_coordenador
#         })
#     return dados

# @request.get("/planos-de-aula/{id}")
# async def obter_plano(id: int, db: Session = Depends(get_db)):
#     """
#     Essa é a rota para obter um plano de aula cadastrado no sistema, identificado pelo id
#     """
#     repo = PlanoAulaRepos()
#     result = repo.buscar_por_id(db, id)
#     if (result is None):
#         return {"Plano de aula não encontrado"}
#     dados = {
#         "id": result.id,
#         "titulo": result.titulo,
#         "descricao": result.descricao,
#         "status": result.status,
#         "id_professor": result.id_professor,
#         "id_coordenador": result.id_coordenador
#     }
#     return {"Plano de aula" : dados}

# @request.post("/planos-de-aula")
# async def criar_plano(
#     titulo: str,           
#     descricao: str,         
#     status: str,           
#     id_professor: int,     
#     id_coordenador: int,   
#     db: Session = Depends(get_db)
# ):
#     """
#     Essa é a rota para criar um plano de aula
#     """
#     repo = PlanoAulaRepos()
#     novo_plano = PlanoAula(
#         titulo=titulo,
#         descricao=descricao,
#         status=status,
#         id_professor=id_professor,
#         id_coordenador=id_coordenador
#     )
#     criado = repo.criar(db, novo_plano)
#     return {
#         "mensagem": "Plano de aula criado com sucesso!",
#         "id": criado.id
#     }

# @request.put("/planos-de-aula/{id}")
# async def atualizar_plano(
#     id: int,
#     titulo: str = Body(None),
#     descricao: str = Body(None),
#     status: str = Body(None),
#     id_professor: int = Body(None),
#     id_coordenador: int = Body(None),
#     db: Session = Depends(get_db)
# ):
#     """
#     Atualiza plano de aula, sendo cada campo é um parâmetro opcional no body
#     """
#     repo = PlanoAulaRepos()
#     plano = repo.buscar_por_id(db, id)
#     if not plano:
#         return {"erro": "Plano de aula não encontrado"}
#     dados = {}
#     if titulo is not None:
#         dados["titulo"] = titulo
#     if descricao is not None:
#         dados["descricao"] = descricao
#     if status is not None:
#         dados["status"] = status
#     if id_professor is not None:
#         dados["id_professor"] = id_professor
#     if id_coordenador is not None:
#         dados["id_coordenador"] = id_coordenador
#     if not dados:
#         return {"erro": "Nenhum dado enviado para atualização"}
#     atualizado = repo.editar(db, id, dados)
#     return {
#         "mensagem": "Plano de aula atualizado com sucesso!",
#         "plano": {
#             "id": atualizado.id,
#             "titulo": atualizado.titulo,
#             "descricao": atualizado.descricao,
#             "status": atualizado.status,
#             "id_professor": atualizado.id_professor,
#             "id_coordenador": atualizado.id_coordenador
#         }
#     }
    
# @request.delete("/planos-de-aula/{id}")
# async def remover_plano(id: int, db: Session = Depends(get_db)):
#     """
#     Essa é a rota para deletar um plano de aula cadastrado no sistema, identificado pelo id
#     """
#     repo = PlanoAulaRepos()
#     result = repo.deletar(db, id)
#     if (result is None):
#         return {"Plano de aula não encontrado"}
#     return{"Plano de aula deletado com sucesso!"}



# ### CRUD - EMPRÉSTIMOS ###

# @request.get("/emprestimos")
# async def listar_emprestimos(db: Session = Depends(get_db)):
#     """
#     Essa é a rota para listar todos os empréstimos cadastrados no sistema
#     """
#     repo = EmprestimoRepos()
#     result = repo.listar(db)
#     if (not result):
#         return {"Não foram encontrados empréstimos cadastrados"}
    
#     dados = []
#     for emprestimo in result:
#         dados.append({
#             "id": emprestimo.id,
#             "quantidade": emprestimo.quantidade,
#             "data_hora": emprestimo.data_hora,
#             "id_escola": emprestimo.id_escola,
#             "id_equipamento": emprestimo.id_equipamento,
#             "id_plano_aula": emprestimo.id_plano_aula
#         })
#     return dados

# # @request.get("/emprestimos/{emprestimo_id}")
# # async def obter_emprestimo(emprestimo_id: int):

# # @request.post("/emprestimos")
# # async def criar_emprestimo(dados):

# # @request.post("/emprestimos/{emprestimo_id}")
# # async def atualizar_emprestimo(emprestimo_id: int, dados):

# # @request.post("/emprestimos/{emprestimo_id}")
# # async def remover_emprestimo(emprestimo_id: int):

# # @request.post("/emprestimos/{emprestimo_id}/avaliacao")
# # async def avaliar_emprestimo(emprestimo_id: int, status):



# ### CRUD - SOLICITAÇÕES ###

# @request.get("/solicitacoes")
# async def listar_solicitacoes(db: Session = Depends(get_db)):
#     """
#     Essa é a rota para listar todos os solicitações de aula cadastrados no sistema
#     """
#     repo = PlanoAulaRepos()
#     result = repo.listar(db)
#     if (not result):
#         return {"Não foram encontrados solicitações cadastradas"}
    
#     dados = []
#     for solicitacao in result:
#         dados.append({
#             "id_administrador": solicitacao.id_administrador,
#             "id_emprestimo": solicitacao.id_emprestimo,
#             "id_coordenador": solicitacao.id_coordenador,
#             "status": solicitacao.status
#         })
#     return dados

# # @request.get("/solicitacoes/{solicitacoes_id}")
# # async def obter_emprestimo(solicitacoes_id: int):

# # @request.post("/solicitacoes")
# # async def criar_emprestimo(dados):

# # @request.post("/solicitacoes/{solicitacoes_id}")
# # async def atualizar_emprestimo(solicitacoes_id: int, dados):

# # @request.post("/solicitacoes/{solicitacoes_id}")
# # async def remover_emprestimo(solicitacoes_id: int):

# # @request.post("/solicitacoes/{solicitacoes_id}/avaliacao")
# # async def avaliar_emprestimo(solicitacoes_id: int, status):



# ### TESTAS AS ROUTES:
# # 1º source venv/bin/activate  
# # 2º uvicorn src.main:app --reload