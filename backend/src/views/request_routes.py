from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database import get_db

# imports dos modelos e schemas
from src.models.plano_aula import PlanoAula, ConsolidacaoPlanoSchema, AprovarPlanoSchema, AtualizarPlanoAulaSchema
from src.models.emprestimo import Emprestimo, EmprestimoSchema, AtualizarEmprestimoSchema
from src.models.solicitacao import Solicitacao, SolicitacaoSchema, ConsolidacaoSolicitacaoSchema, AtualizarSolicitacaoSchema

# imports dos repositórios
from src.repositories.plano_aula import PlanoAulaRepos
from src.repositories.emprestimo import EmprestimoRepos
from src.repositories.solicitacao import SolicitacaoRepos
from src.repositories.coordenador import CoordenadorRepos
from src.repositories.administrador import AdministradorRepo
from src.repositories.professor import ProfessorRepos 
from pydantic import BaseModel

request = APIRouter(prefix="/requisicao", tags=["request"])

# schema específico para não exigir id_coordenador do professor
class PlanoAulaCreateSchema(BaseModel):
    titulo: str
    descricao: str
    status: str
    id_professor: int

# CRUD - PLANOS DE AULA

@request.get("/planos-de-aula")
async def listar_planos(db: Session = Depends(get_db)):
    """Busca todos os planos no banco de dados"""
    repo = PlanoAulaRepos()
    return repo.listar(db)

@request.get("/planos-de-aula/professor/{matricula}")
async def listar_planos_do_professor(matricula: int, db: Session = Depends(get_db)):
    """Lista apenas os planos criados pelo professor logado"""
    repo = PlanoAulaRepos()
    return repo.listar_por_professor(db, matricula)

@request.get("/planos-de-aula/coordenador/{matricula}")
async def listar_planos_por_coordenador(matricula: int, db: Session = Depends(get_db)):
    """Lista planos da escola do coordenador logado"""
    repo_coord = CoordenadorRepos()
    coordenador = repo_coord.buscar_por_id(db, matricula)
    
    if not coordenador:
        raise HTTPException(status_code=404, detail="Coordenador não encontrado")

    repo_plano = PlanoAulaRepos()
   
    return repo_plano.listar_por_escola(db, int(coordenador.id_escola)) # type: ignore

@request.get("/planos-de-aula/administrador/{matricula}")
async def listar_planos_para_admin(matricula: int, db: Session = Depends(get_db)):
    """Busca planos ENVIADOS do bairro do administrador"""
    repo_admin = AdministradorRepo()
    admin = repo_admin.buscar_por_id(db, matricula)
    
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador não encontrado")
    
    repo_plano = PlanoAulaRepos()
    return repo_plano.listar_pendentes_por_bairro(db, admin.bairro) # type: ignore

@request.post("/planos-de-aula")
async def criar_plano(dados: PlanoAulaCreateSchema, db: Session = Depends(get_db)):
    """Professor cria plano. Coordenador é descoberto automaticamente."""
   
    repo_prof = ProfessorRepos()
    professor = repo_prof.buscar_por_id(db, dados.id_professor)
    if not professor:
        raise HTTPException(status_code=404, detail="Professor não encontrado")

    repo_coord = CoordenadorRepos()
    coordenador = repo_coord.buscar_por_escola(db, int(professor.id_escola)) # type: ignore
    
    if not coordenador:
        raise HTTPException(status_code=400, detail="Nenhum coordenador encontrado para sua escola. Contate o suporte.")

    repo_plano = PlanoAulaRepos()
    novo_plano = PlanoAula(
        titulo=dados.titulo,
        descricao=dados.descricao,
        status=dados.status,
        id_professor=dados.id_professor,
        id_coordenador=coordenador.matricula
    )
    repo_plano.criar(db, novo_plano)
    return {"mensagem": "Plano criado com sucesso!", "id": novo_plano.id}

@request.put("/planos-de-aula/{id}")
async def atualizar_plano(id: int, dados: AtualizarPlanoAulaSchema, db: Session = Depends(get_db)):
    repo = PlanoAulaRepos()
    
    atualizado = repo.editar(db, id, dados.dict(exclude_unset=True))
    
    if atualizado is None:
        raise HTTPException(status_code=404, detail="Plano não encontrado")

    return {
        "mensagem": "Plano atualizado com sucesso!",
        "plano": {
            "id": atualizado.id,
            "titulo": atualizado.titulo,
            "status": atualizado.status
        }
    }

@request.post("/planos-de-aula/consolidar")
async def consolidar_planos(dados: ConsolidacaoPlanoSchema, db: Session = Depends(get_db)):
    """Muda status para ENVIADO"""
    repo = PlanoAulaRepos()
    count = 0
    for id_plano in dados.planos_ids:
        plano = repo.editar(db, id_plano, {"status": "ENVIADO"})
        if plano:
            count += 1
    return {"mensagem": f"{count} planos enviados para a administração!"}

@request.put("/planos-de-aula/{id}/avaliacao")
async def avaliar_plano(id: int, dados: AprovarPlanoSchema, db: Session = Depends(get_db)):
    repo = PlanoAulaRepos()
    atualizado = repo.editar(db, id, {"status": dados.status})
    
    if atualizado is None:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
        
    return {"mensagem": f"Plano atualizado para {dados.status}!"}

@request.delete("/planos-de-aula/{id}")
async def deletar_plano(id: int, db: Session = Depends(get_db)):
    repo = PlanoAulaRepos()
    if not repo.deletar(db, id):
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return {"mensagem": "Plano removido com sucesso"}

@request.get("/emprestimos")
async def listar_emprestimos(db: Session = Depends(get_db)):
    repo = EmprestimoRepos()
    return repo.listar(db)

@request.get("/emprestimos/{id}")
async def obter_emprestimo(id: int, db: Session = Depends(get_db)):
    repo = EmprestimoRepos()
    emprestimo = repo.buscar_por_id(db, id)
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    return emprestimo

@request.post("/emprestimos")
async def criar_emprestimo(dados: EmprestimoSchema, db: Session = Depends(get_db)):
    repo = EmprestimoRepos()
    novo = Emprestimo(
        quantidade=dados.quantidade,
        id_escola=dados.id_escola,
        id_equipamento=dados.id_equipamento,
        id_plano_aula=dados.id_plano_aula
    )
    novo.data_hora = dados.data_hora # type: ignore
    
    repo.criar(db, novo)
    return {"mensagem": "Empréstimo criado com sucesso!", "id": novo.id}

@request.put("/emprestimos/{id}")
async def atualizar_emprestimo(id: int, dados: AtualizarEmprestimoSchema, db: Session = Depends(get_db)):
    repo = EmprestimoRepos()
    atualizado = repo.editar(db, id, dados.dict(exclude_unset=True))
    if atualizado is None:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    return {"mensagem": "Empréstimo atualizado!", "emprestimo": atualizado}

@request.delete("/emprestimos/{id}")
async def deletar_emprestimo(id: int, db: Session = Depends(get_db)):
    repo = EmprestimoRepos()
    if not repo.deletar(db, id):
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    return {"mensagem": "Empréstimo removido com sucesso"}


# CRUD - SOLICITAÇÕES

@request.get("/solicitacoes")
async def listar_solicitacoes(db: Session = Depends(get_db)):
    repo = SolicitacaoRepos()
    return repo.listar(db)

@request.post("/solicitacoes")
async def criar_solicitacao(dados: SolicitacaoSchema, db: Session = Depends(get_db)):
    repo = SolicitacaoRepos()

    nova = Solicitacao(
        id_administrador=dados.id_servidor, 
        id_emprestimo=dados.id_emprestimo,
        id_coordenador=dados.id_coordenador,
        status=dados.status
    )
    repo.criar(db, nova)
    return {"mensagem": "Solicitação criada com sucesso!"}

@request.post("/solicitacoes/consolidar")
async def consolidar_solicitacoes(dados: ConsolidacaoSolicitacaoSchema, db: Session = Depends(get_db)):
    repo = SolicitacaoRepos()
    count = 0
    for ids in dados.solicitacoes_ids:

        item = repo.editar(
            db,
            ids["id_servidor"],
            ids["id_emprestimo"],
            ids["id_coordenador"],
            {"status": "ENVIADO"}
        )
        if item: count += 1
    return {"mensagem": f"{count} solicitações enviadas!"}

@request.put("/solicitacoes/{id_servidor}/{id_emprestimo}/{id_coordenador}")
async def atualizar_solicitacao(
    id_servidor: int, id_emprestimo: int, id_coordenador: int,
    dados: AtualizarSolicitacaoSchema, db: Session = Depends(get_db)
):
    repo = SolicitacaoRepos()
    atualizado = repo.editar(
        db, id_servidor, id_emprestimo, id_coordenador,
        {"status": dados.status}
    )
    if atualizado is None:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")
    return {"mensagem": f"Solicitação atualizada para {dados.status}!"}

@request.delete("/solicitacoes/{id_servidor}/{id_emprestimo}/{id_coordenador}")
async def deletar_solicitacao(id_servidor: int, id_emprestimo: int, id_coordenador: int, db: Session = Depends(get_db)):
    repo = SolicitacaoRepos()
    if not repo.deletar(db, id_servidor, id_emprestimo, id_coordenador):
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")
    return {"mensagem": "Solicitação removida com sucesso"}

# Equipamentos
@request.get("/equipamentos")
async def listar_equipamentos():
    return {"mensagem": "Rota de equipamentos ainda não implementada."}