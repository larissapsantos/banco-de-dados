from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.plano_aula import ConsolidacaoPlanoSchema, AprovarPlanoSchema, AtualizarPlanoAulaSchema, PlanoAulaSchema
from src.models.emprestimo import EmprestimoSchema, AtualizarEmprestimoSchema
from src.models.solicitacao import SolicitacaoSchema, ConsolidacaoSolicitacaoSchema, AtualizarSolicitacaoSchema
from src.repositories.plano_aula import PlanoAulaRepos
from src.repositories.emprestimo import EmprestimoRepos
from src.repositories.solicitacao import SolicitacaoRepos
from src.repositories.coordenador import CoordenadorRepos
from src.repositories.administrador import AdministradorRepo
from src.repositories.professor import ProfessorRepos 
from src.repositories.equipamento import EquipamentoRepos

request = APIRouter(prefix="/requisicao", tags=["request"])


# CRUD - PLANOS DE AULA

@request.get("/planos-de-aula")
async def listar_planos(db: Session = Depends(get_db)):
    repo = PlanoAulaRepos()
    return repo.listar(db)

@request.get("/planos-de-aula/professor/{matricula}")
async def listar_planos_do_professor(matricula: int, db: Session = Depends(get_db)):
    repo = PlanoAulaRepos()
    return repo.listar_por_professor(db, matricula)

@request.get("/planos-de-aula/coordenador/{matricula}")
async def listar_planos_por_coordenador(matricula: int, db: Session = Depends(get_db)):
    repo_coord = CoordenadorRepos()
    coordenador = repo_coord.buscar_por_id(db, matricula)
    
    if not coordenador:
        raise HTTPException(status_code=404, detail="Coordenador não encontrado")

    repo_plano = PlanoAulaRepos()
   
    return repo_plano.listar_por_escola(db, int(coordenador.id_escola)) 

@request.get("/planos-de-aula/administrador/{matricula}")
async def listar_planos_para_admin(matricula: int, db: Session = Depends(get_db)):
    repo_admin = AdministradorRepo()
    admin = repo_admin.buscar_por_id(db, matricula)
    
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador não encontrado")
    
    repo_plano = PlanoAulaRepos()
    return repo_plano.listar_pendentes_por_bairro(db, admin.bairro) 

@request.post("/planos-de-aula")
async def criar_plano(dados: PlanoAulaSchema, db: Session = Depends(get_db)):
    repo_prof = ProfessorRepos()
    professor = repo_prof.buscar_por_id(db, dados.id_professor)
    if not professor:
        raise HTTPException(status_code=404, detail="Professor não encontrado")

    repo_coord = CoordenadorRepos()
    coordenadores = repo_coord.buscar_por_escola(db, int(professor.id_escola))
    coordenador = next((c for c in coordenadores if c.matricula == dados.id_coordenador), None)
    if not coordenador:
        raise HTTPException(status_code=400, detail="Nenhum coordenador encontrado para sua escola. Contate o suporte.")

    repo_plano = PlanoAulaRepos()
    novo_plano = PlanoAulaSchema(
        titulo=dados.titulo,
        descricao=dados.descricao,
        status=dados.status,
        id_professor=dados.id_professor,
        id_coordenador=coordenador.matricula
    )
    resultado = repo_plano.criar(db, novo_plano.model_dump())
    if resultado is None:
        raise HTTPException(status_code=400, detail="Não foi possível criar o plano de aula.")
    
    return {"mensagem": "Plano criado com sucesso!"}

@request.put("/planos-de-aula/{id}")
async def atualizar_plano(id: int, dados: AtualizarPlanoAulaSchema, db: Session = Depends(get_db)):
    repo = PlanoAulaRepos()
    
    atualizado = repo.editar(db, id, dados.dict(exclude_unset=True))
    
    if atualizado is None:
        raise HTTPException(status_code=400, detail="Não foi possível deletar o plano de aula.")

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

# CRUD - EMPRÉSTIMOS

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
    novo = EmprestimoSchema(
        id_escola=dados.id_escola,
        id_equipamento=dados.id_equipamento,
        id_plano_aula=dados.id_plano_aula
    )
    novo.data_hora = dados.data_hora
    
    result = repo.criar(db, novo.model_dump())
    if result is None:
        raise HTTPException(status_code=400, detail="Falha ao criar empréstimo.")
    return {"mensagem": "Empréstimo criado com sucesso!", "id": result.id}

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
    if not repo.excluir(db, id):
        raise HTTPException(status_code=404, detail="Esse empréstimo não pode ser deletado")
    return {"mensagem": "Empréstimo removido com sucesso"}


# CRUD - SOLICITAÇÕES

@request.get("/solicitacoes")
async def listar_solicitacoes(db: Session = Depends(get_db)):
    repo = SolicitacaoRepos()
    return repo.listar(db)

@request.post("/solicitacoes")
async def criar_solicitacao(dados: SolicitacaoSchema, db: Session = Depends(get_db)):
    repo = SolicitacaoRepos()

    nova = SolicitacaoSchema(
        id_servidor=dados.id_servidor, 
        id_emprestimo=dados.id_emprestimo,
        id_coordenador=dados.id_coordenador,
        status=dados.status
    )
    repo.criar(db, nova.model_dump())
    return {"mensagem": "Solicitação criada com sucesso!"}

@request.post("/solicitacoes/consolidar")
async def consolidar_solicitacoes(dados: ConsolidacaoSolicitacaoSchema, db: Session = Depends(get_db)):
    repo = SolicitacaoRepos()
    count = 0
    for solicitacao in dados.model_dump()["solicitacoes_ids"]:
        item = repo.editar(
            db,
            solicitacao["id_servidor"],
            solicitacao["id_emprestimo"],
            solicitacao["id_coordenador"],
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
async def listar_equipamentos(db: Session = Depends(get_db)):
    repo = EquipamentoRepos()
    return repo.listar(db)

@request.get("/equipamentos/{id}")
async def listar_equipamentos(id: int,db: Session = Depends(get_db)):
    repo = EquipamentoRepos()
    return repo.buscar_por_id(db, id)