from fastapi import APIRouter

request = APIRouter(prefix="/requisicao", tags=["request"])

### CRUD - PLANOS DE AULA ###

@request.get("/")
async def requisicao():
    """
    Essa é a rota padrão de requisição do sistema. Todas as rotas de requisição precisam de autenticação
    """
    return{"mensagem": "Você acessou a rota padrão de requisicao"}

@request.get("/planos-de-aula")
async def listar_planos():
    """
    Essa é a rota para listar todos os planos de aula cadastrados no sistema
    """
    return{"mensagem": "Você acessou a lista de planos de aula"}
    

# @request.get("/planos-de-aula/{plano_id}")
# async def obter_plano(plano_id: int):
#     return{"mensagem": "Você acessou a um único plano de aula"}

# @request.post("/planos-de-aula")
# async def criar_plano(dados):

# @request.post("/planos-de-aula/{plano_id}")
# async def atualizar_plano(plano_id: int, dados)
    
# @request.post("/planos-de-aula/{plano_id}")
# async def remover_plano(plano_id: int):

### CRUD - EMPRÉSTIMOS ###

@request.get("/emprestimos")
async def listar_emprestimos():
    """
    Essa é a rota para listar todos os empréstimos cadastrados no sistema
    """
    return{"mensagem": "Você acessou a lista de empréstimos"}

# @request.get("/emprestimos/{emprestimo_id}")
# async def obter_emprestimo(emprestimo_id: int):
#     return{"mensagem": "Você acessou a um único empréstimo"}

# @request.post("/emprestimos")
# async def criar_emprestimo(dados):

# @request.post("/emprestimos/{emprestimo_id}")
# async def atualizar_emprestimo(emprestimo_id: int, dados):

# @request.post("/emprestimos/{emprestimo_id}")
# async def remover_emprestimo(emprestimo_id: int):

# @request.post("/emprestimos/{emprestimo_id}/avaliacao")
# async def avaliar_emprestimo(emprestimo_id: int, status):