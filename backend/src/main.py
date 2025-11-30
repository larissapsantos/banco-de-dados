from fastapi import FastAPI

app = FastAPI()

from src.auth_routes import auth
from src.request_routes import request

app.include_router(auth)
app.include_router(request)

# Para rodar o código, executar no terminal: uvicorn src.main:app --reload

# endpoints: /tela-inicial ou /tela-login

# REST APIS
# Get - leitura/pegar
# Post - enviar/criar
# Put - edição
# Delete - deletar