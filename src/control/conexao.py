import pymysql

def criar_conexao():
    try:
        conexao = pymysql.connect(
        host = "localhost",
        user = "root",            # usuário do MySQL
        password = "bE9b-zavq1116",   # senha
        database = "emprestimoescolar",
        charset = "utf8mb4",
        cursorclass = pymysql.cursors.DictCursor,  # resultado vem como dicionário
        autocommit = True
        )

        print("Conexão concluída!")
        return conexao
    
    except Exception as erro:
        print("Erro ao conectar:", erro)
        return None

