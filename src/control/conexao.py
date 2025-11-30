import pymysql

def criar_conexao():
    try:
        conexao = pymysql.connect(
        host = " ",
        user = " ", 
        password = " ",   
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

