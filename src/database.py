from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base

# Conexão com o BD
db = create_engine(
    "mysql+pymysql://root@localhost:3306/emprestimoEscolar",
    echo=True
)

# Base do BD
Base = declarative_base()

# TESTE CONEXÃO

# try:
#     with db.connect() as conn:
#         result = conn.execute(text("SELECT 1"))
#         print("Conexão funcionando:", result.fetchone())
# except Exception as e:
#     print("Erro na conexão:", e)