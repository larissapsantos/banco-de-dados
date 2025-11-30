from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root@localhost:3306/projetoBD"

# Gerencia a conexão com o BD
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Permite que as classes representem tabelas no BD
Base = declarative_base()

## TESTE CONEXÃO ###
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Conexão funcionando:", result.fetchone())
except Exception as e:
    print("Erro na conexão:", e)

# Criar novas migrações normalmente:
# alembic revision --autogenerate -m "Minha nova alteração"

# Aplicar a migração:
# alembic upgrade head

# Verificar a integração com o bd:
# alembic current 