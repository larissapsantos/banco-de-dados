from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database import get_db
from src.models.plano_aula import PlanoAula, PlanoAulaSchema, ConsolidacaoPlanoSchema, AprovarPlanoSchema, AtualizarPlanoAulaSchema
from src.models.emprestimo import Emprestimo, EmprestimoSchema, AtualizarEmprestimoSchema
from src.models.solicitacao import Solicitacao, SolicitacaoSchema, ConsolidacaoSolicitacaoSchema, AtualizarSolicitacaoSchema
from src.repositories.plano_aula import PlanoAulaRepos
from src.repositories.emprestimo import EmprestimoRepos
from src.repositories.solicitacao import SolicitacaoRepos
from src.repositories.coordenador import CoordenadorRepos
from src.repositories.administrador import AdministradorRepo

request = APIRouter(prefix="/requisicao", tags=["request"])



### ROTAS DE LEITURA DE PLANOS DE AULA (GET) ###

@request.get("/planos-de-aula")
async def listar_planos(db: Session = Depends(get_db)):
    """
    Busca todos os planos de aula no banco de dados
    """
    repo = PlanoAulaRepos()
    planos = repo.listar(db)
    return planos

@request.get("/planos-de-aula/coordenador/{matricula}")
async def listar_planos_por_coordenador(matricula: int, db: Session = Depends(get_db)):
    """
    Lista os planos de aula somente da escola do coordenador logado
    """
    repo_coord = CoordenadorRepos()
    coordenador = repo_coord.buscar_por_id(db, matricula)
    
    if not coordenador:
        raise HTTPException(status_code=404, detail="Coordenador não encontrado")

    repo_plano = PlanoAulaRepos()
    planos = repo_plano.listar_por_escola(db, coordenador.id_escola)
    return planos

@request.get("/planos-de-aula/administrador/{matricula}")
async def listar_planos_para_admin(matricula: int, db: Session = Depends(get_db)):
    """
    Descobre o bairro do administrador e busca os planos de aula do mesmo bairro da escola do coordenador logado
    """
    repo_admin = AdministradorRepo()
    admin = repo_admin.buscar_por_id(db, matricula)
    
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador não encontrado")
    
    repo_plano = PlanoAulaRepos()
    planos = repo_plano.listar_pendentes_por_bairro(db, admin.bairro)
    return planos

### ROTAS DE ESCRITA DE PLANOS DE AULA (POST/PUT/DELETE) ###

@request.post("/planos-de-aula")
async def criar_plano(dados: PlanoAulaSchema, db: Session = Depends(get_db)):
    """
    Professor cria um novo plano de aula
    """
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

@request.put("/planos-de-aula/{id}")
async def atualizar_plano(id: int, dados: AtualizarPlanoAulaSchema, db: Session = Depends(get_db)):
    """
    Atualiza campos opcionais de um plano de aula
    """
    repo = PlanoAulaRepos()

    existente = repo.buscar_por_id(db, id)
    if not existente:
        raise HTTPException(status_code=404, detail="Plano não encontrado")

    atualizado = repo.editar(db, id, dados.dict(exclude_unset=True))

    return {
        "mensagem": "Plano de aula atualizado com sucesso!",
        "plano": atualizado
    }

@request.post("/planos-de-aula/consolidar")
async def consolidar_planos(dados: ConsolidacaoPlanoSchema, db: Session = Depends(get_db)):
    """
    Coordenador envia os planos de aula para a administração
    """
    repo = PlanoAulaRepos()
    for id_plano in dados.planos_ids:
        plano = repo.editar(db, id_plano, {"status": "ENVIADO"})
        if not plano:
            print(f"Aviso: Plano {id_plano} não encontrado ao consolidar.")
            
    return {"mensagem": f"{len(dados.planos_ids)} planos enviados para a administração!"}

@request.put("/planos-de-aula/{id}/avaliacao")
async def avaliar_plano(id: int, dados: AprovarPlanoSchema, db: Session = Depends(get_db)):
    """
    Administrador aprova ou rejeita o plano de aula
    """
    repo = PlanoAulaRepos()
    atualizado = repo.editar(db, id, {"status": dados.status})
    if atualizado is None:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return {"mensagem": f"Plano atualizado para {dados.status}!"}

@request.delete("/planos-de-aula/{id}")
async def deletar_plano(id: int, db: Session = Depends(get_db)):
    """
    Remove um plano de aula pelo ID
    """
    repo = PlanoAulaRepos()
    sucesso = repo.deletar(db, id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return {"mensagem": "Plano removido com sucesso"}



### ROTAS DE LEITURA DE EMPRÉSTIMOS (GET) ###

@request.get("/emprestimos")
async def listar_emprestimos(db: Session = Depends(get_db)):
    """
    Lista todos os empréstimos cadastrados
    """
    repo = EmprestimoRepos()
    emprestimos = repo.listar(db)
    return emprestimos


@request.get("/emprestimos/{id}")
async def obter_emprestimo(id: int, db: Session = Depends(get_db)):
    """
    Busca um empréstimo pelo ID
    """
    repo = EmprestimoRepos()
    emprestimo = repo.buscar_por_id(db, id)

    if not emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

    return emprestimo

### ROTAS DE ESCRITA DE EMPRÉSTIMO (POST/PUT/DELETE) ###

@request.post("/emprestimos")
async def criar_emprestimo(dados: EmprestimoSchema, db: Session = Depends(get_db)):
    """
    Cria um empréstimo
    """
    repo = EmprestimoRepos()

    novo = Emprestimo(
        quantidade=dados.quantidade,
        data_hora=dados.data_hora,
        id_escola=dados.id_escola,
        id_equipamento=dados.id_equipamento,
        id_plano_aula=dados.id_plano_aula
    )

    repo.criar(db, novo)
    return {"mensagem": "Empréstimo criado com sucesso!", "id": novo.id}


@request.put("/emprestimos/{id}")
async def atualizar_emprestimo(id: int, dados: AtualizarEmprestimoSchema, db: Session = Depends(get_db)):
    """
    Atualiza campos opcionais de um empréstimo
    """
    repo = EmprestimoRepos()

    existente = repo.buscar_por_id(db, id)
    if not existente:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

    atualizado = repo.editar(db, id, dados.dict(exclude_unset=True))

    return {
        "mensagem": "Empréstimo atualizado com sucesso!",
        "emprestimo": atualizado
    }


@request.delete("/emprestimos/{id}")
async def deletar_emprestimo(id: int, db: Session = Depends(get_db)):
    """
    Remove um empréstimo pelo ID
    """
    repo = EmprestimoRepos()
    removido = repo.deletar(db, id)

    if not removido:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

    return {"mensagem": "Empréstimo removido com sucesso"}

@request.get("/solicitacoes")
async def listar_solicitacoes(db: Session = Depends(get_db)):
    """
    Busca todas as solicitações no banco de dados
    """
    repo = SolicitacaoRepos()
    solicitacoes = repo.listar(db)
    return solicitacoes



### ROTAS DE LEITURA DE SOLICITAÇÕES (GET) ###

@request.get("/solicitacoes/coordenador/{matricula}")
async def listar_solicitacoes_por_coordenador(matricula: int, db: Session = Depends(get_db)):
    """
    Lista as solicitações associadas à escola do coordenador logado
    """
    repo_coord = CoordenadorRepos()
    coordenador = repo_coord.buscar_por_id(db, matricula)
    
    if not coordenador:
        raise HTTPException(status_code=404, detail="Coordenador não encontrado")

    repo_solicitacao = SolicitacaoRepos()
    solicitacoes = repo_solicitacao.listar_por_escola(db, coordenador.id_escola)
    return solicitacoes

@request.get("/solicitacoes/administrador/{matricula}")
async def listar_solicitacoes_para_admin(matricula: int, db: Session = Depends(get_db)):
    """
    Descobre o bairro do administrador e busca as solicitações da mesma região
    """
    repo_admin = AdministradorRepo()
    admin = repo_admin.buscar_por_id(db, matricula)
    
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador não encontrado")
    
    repo_solicitacao = SolicitacaoRepos()
    solicitacoes = repo_solicitacao.listar_pendentes_por_bairro(db, admin.bairro)
    return solicitacoes

### ROTAS DE ESCRITA DE SOLICITAÇÕES (POST/PUT/DELETE) ###

@request.post("/solicitacoes")
async def criar_solicitacao(dados: SolicitacaoSchema, db: Session = Depends(get_db)):
    """
    Cria uma nova solicitação
    """
    repo = SolicitacaoRepos()
    nova_solicitacao = Solicitacao(
        id_servidor=dados.id_servidor,
        id_emprestimo=dados.id_emprestimo,
        id_coordenador=dados.id_coordenador,
        status=dados.status
    )
    repo.criar(db, nova_solicitacao)
    return {
        "mensagem": "Solicitação criada com sucesso!",
        "ids": {
            "id_servidor": nova_solicitacao.id_servidor,
            "id_emprestimo": nova_solicitacao.id_emprestimo,
            "id_coordenador": nova_solicitacao.id_coordenador
        }
    }

@request.post("/solicitacoes/consolidar")
async def consolidar_solicitacoes(dados: ConsolidacaoSolicitacaoSchema, db: Session = Depends(get_db)):
    """
    Coordenador envia as solicitações para a administração
    """
    repo = SolicitacaoRepos()
    for ids in dados.solicitacoes_ids:
        solicitacao = repo.editar(
            db,
            ids["id_servidor"],
            ids["id_emprestimo"],
            ids["id_coordenador"],
            {"status": "ENVIADO"}
        )
        if not solicitacao:
            print(f"Aviso: Solicitação {ids} não encontrada ao consolidar.")
            
    return {"mensagem": f"{len(dados.solicitacoes_ids)} solicitações enviadas para a administração!"}

@request.put("/solicitacoes/{id_servidor}/{id_emprestimo}/{id_coordenador}")
async def atualizar_solicitacao(
    id_servidor: int,
    id_emprestimo: int,
    id_coordenador: int,
    dados: AtualizarSolicitacaoSchema,
    db: Session = Depends(get_db)
):
    """
    Atualiza o status da solicitação
    """
    repo = SolicitacaoRepos()
    atualizado = repo.editar(
        db,
        id_servidor,
        id_emprestimo,
        id_coordenador,
        {"status": dados.status}
    )
    if atualizado is None:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")
    return {"mensagem": f"Solicitação atualizada para {dados.status}!"}

@request.delete("/solicitacoes/{id_servidor}/{id_emprestimo}/{id_coordenador}")
async def deletar_solicitacao(id_servidor: int, id_emprestimo: int, id_coordenador: int, db: Session = Depends(get_db)):
    """
    Remove uma solicitação pelo ID composto
    """
    repo = SolicitacaoRepos()
    sucesso = repo.deletar(db, id_servidor, id_emprestimo, id_coordenador)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")
    return {"mensagem": "Solicitação removida com sucesso"}



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

# @request.get("/emprestimos/{id}")
# async def obter_emprestimo(id: int, db: Session = Depends(get_db)):
#     """
#     Essa é a rota para obter um empréstimo cadastrado no sistema, identificado pelo id
#     """
#     repo = EmprestimoRepos()
#     result = repo.buscar_por_id(db, id)
#     if (result is None):
#         return {"Empréstimo não encontrado"}
#     dados = {
#         "id": result.id,
#         "quantidade": result.quantidade,
#         "data_hora": result.data_hora,
#         "id_escola": result.id_escola,
#         "id_equipamento": result.id_equipamento,
#         "id_plano_aula": result.id_plano_aula
#     }
#     return {"Empréstimo": dados}

# @request.post("/emprestimos")
# async def criar_emprestimo(
#     quantidade: int,
#     data_hora: str,
#     id_escola: int,
#     id_equipamento: int,
#     id_plano_aula: int,
#     db: Session = Depends(get_db)
# ):
#     """
#     Essa é a rota para criar um empréstimo
#     """
#     repo = EmprestimoRepos()
#     novo_emprestimo = Emprestimo(
#         quantidade=quantidade,
#         data_hora=data_hora,
#         id_escola=id_escola,
#         id_equipamento=id_equipamento,
#         id_plano_aula=id_plano_aula
#     )
#     criado = repo.criar(db, novo_emprestimo)
#     return {
#         "mensagem": "Empréstimo criado com sucesso!",
#         "id": criado.id
#     }

# @request.put("/emprestimos/{id}")
# async def atualizar_emprestimo(
#     id: int,
#     quantidade: int = Body(None),
#     data_hora: str = Body(None),
#     id_escola: int = Body(None),
#     id_equipamento: int = Body(None),
#     id_plano_aula: int = Body(None),
#     db: Session = Depends(get_db)
# ):
#     """
#     Atualiza empréstimo, sendo cada campo é um parâmetro opcional no body
#     """
#     repo = EmprestimoRepos()
#     emprestimo = repo.buscar_por_id(db, id)
#     if not emprestimo:
#         return {"erro": "Empréstimo não encontrado"}
#     dados = {}
#     if quantidade is not None:
#         dados["quantidade"] = quantidade
#     if data_hora is not None:
#         dados["data_hora"] = data_hora
#     if id_escola is not None:
#         dados["id_escola"] = id_escola
#     if id_equipamento is not None:
#         dados["id_equipamento"] = id_equipamento
#     if id_plano_aula is not None:
#         dados["id_plano_aula"] = id_plano_aula
#     if not dados:
#         return {"erro": "Nenhum dado enviado para atualização"}
#     atualizado = repo.editar(db, id, dados)
#     return {
#         "mensagem": "Empréstimo atualizado com sucesso!",
#         "emprestimo": {
#             "id": atualizado.id,
#             "quantidade": atualizado.quantidade,
#             "data_hora": atualizado.data_hora,
#             "id_escola": atualizado.id_escola,
#             "id_equipamento": atualizado.id_equipamento,
#             "id_plano_aula": atualizado.id_plano_aula
#         }
#     }

# @request.delete("/emprestimos/{id}")
# async def remover_emprestimo(id: int, db: Session = Depends(get_db)):
#     """
#     Essa é a rota para deletar um empréstimo cadastrado no sistema, identificado pelo id
#     """
#     repo = EmprestimoRepos()
#     result = repo.deletar(db, id)
#     if (result is None):
#         return {"Empréstimo não encontrado"}
#     return {"Empréstimo deletado com sucesso!"}



# ### CRUD - SOLICITAÇÕES ###

# @request.get("/solicitacoes")
# async def listar_solicitacoes(db: Session = Depends(get_db)):
#     """
#     Essa é a rota para listar todas as solicitações cadastradas no sistema.
#     """
#     repo = SolicitacaoRepos()
#     result = repo.listar(db)

#     if not result:
#         return {"mensagem": "Não foram encontradas solicitações cadastradas."}

#     dados = []
#     for solicitacao in result:
#         dados.append({
#             "id_administrador": solicitacao.id_administrador,
#             "id_coordenador": solicitacao.id_coordenador,
#             "id_emprestimo": solicitacao.id_emprestimo,
#             "status": solicitacao.status
#         })
#     return dados

# @request.get("/solicitacoes/{id_administrador}/{id_coordenador}/{id_emprestimo}")
# async def obter_solicitacao(id_administrador: int, id_coordenador: int, id_emprestimo: int, db: Session = Depends(get_db)):
#     """
#     Busca uma solicitação pela chave primária composta.
#     """
#     repo = SolicitacaoRepo()
#     result = repo.buscar(db, id_administrador, id_coordenador, id_emprestimo)

#     if not result:
#         return {"mensagem": "Solicitação não encontrada."}

#     return {
#         "solicitacao": {
#             "id_administrador": result.id_administrador,
#             "id_coordenador": result.id_coordenador,
#             "id_emprestimo": result.id_emprestimo,
#             "status": result.status
#         }
#     }

# @request.post("/solicitacoes")
# async def criar_solicitacao(
#     id_administrador: int,
#     id_coordenador: int,
#     id_emprestimo: int,
#     status: str,
#     db: Session = Depends(get_db)
# ):
#     """
#     Cria uma nova solicitação (PK composta impede duplicação)
#     """
#     repo = SolicitacaoRepos()

#     existente = repo.buscar(db, id_administrador, id_coordenador, id_emprestimo)
#     if existente:
#         return {"erro": "Solicitação já existe com essa chave composta."}

#     nova = Solicitacao(
#         id_administrador=id_administrador,
#         id_coordenador=id_coordenador,
#         id_emprestimo=id_emprestimo,
#         status=status
#     )

#     criado = repo.criar(db, nova)
#     return {
#         "mensagem": "Solicitação criada com sucesso!",
#         "solicitacao": {
#             "id_administrador": criado.id_administrador,
#             "id_coordenador": criado.id_coordenador,
#             "id_emprestimo": criado.id_emprestimo,
#             "status": criado.status
#         }
#     }

# @request.put("/solicitacoes/{id_administrador}/{id_coordenador}/{id_emprestimo}")
# async def atualizar_solicitacao(
#     id_administrador: int,
#     id_coordenador: int,
#     id_emprestimo: int,
#     status: str = Body(None),
#     db: Session = Depends(get_db)
# ):
#     """
#     Atualiza uma solicitação existente
#     """
#     repo = SolicitacaoRepos()

#     solicitacao = repo.buscar(db, id_administrador, id_coordenador, id_emprestimo)
#     if not solicitacao:
#         return {"erro": "Solicitação não encontrada."}

#     dados = {}
#     if status is not None:
#         dados["status"] = status

#     if not dados:
#         return {"erro": "Nenhum dado enviado para atualização."}

#     atualizado = repo.editar(db, solicitacao, dados)
#     return {
#         "mensagem": "Solicitação atualizada com sucesso!",
#         "solicitacao": {
#             "id_administrador": atualizado.id_administrador,
#             "id_coordenador": atualizado.id_coordenador,
#             "id_emprestimo": atualizado.id_emprestimo,
#             "status": atualizado.status
#         }
#     }

# @request.delete("/solicitacoes/{id_administrador}/{id_coordenador}/{id_emprestimo}")
# async def remover_solicitacao(id_administrador: int, id_coordenador: int, id_emprestimo: int, db: Session = Depends(get_db)):
#     """
#     Remove uma solicitação pela chave primária composta.
#     """
#     repo = SolicitacaoRepos()
#     solicitacao = repo.buscar(db, id_administrador, id_coordenador, id_emprestimo)

#     if not solicitacao:
#         return {"mensagem": "Solicitação não encontrada."}

#     repo.deletar(db, solicitacao)
#     return {"mensagem": "Solicitação deletada com sucesso!"}

# @request.put("/solicitacoes/{id_administrador}/{id_coordenador}/{id_emprestimo}/avaliacao")
# async def avaliar_solicitacao(
#     id_administrador: int,
#     id_coordenador: int,
#     id_emprestimo: int,
#     status: str,
#     db: Session = Depends(get_db)
# ):
#     """
#     Atualiza o status da solicitação (aprovar/reprovar).
#     """
#     repo = SolicitacaoRepos()
#     solicitacao = repo.buscar(db, id_administrador, id_coordenador, id_emprestimo)

#     if not solicitacao:
#         return {"erro": "Solicitação não encontrada."}

#     solicitacao.status = status
#     db.commit()
#     db.refresh(solicitacao)

#     return {
#         "mensagem": "Status atualizado!",
#         "status": solicitacao.status
#     }



# ### TESTAS AS ROUTES:
# # 1º source venv/bin/activate  
# # 2º uvicorn src.main:app --reload