from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

# Lê as variáveis do arquivo .env
load_dotenv()

# Busca em .env a variável chamada DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Gerencia a conexão com o BD
bd = create_engine(DATABASE_URL, echo=True)

# Permite que as classes representem tabelas no BD
Base = declarative_base()



## TESTE CONEXÃO ###

# try:
#     with bd.connect() as conn:
#         result = conn.execute(text("SELECT 1"))
#         print("Conexão funcionando:", result.fetchone())
# except Exception as e:
#     print("Erro na conexão:", e)