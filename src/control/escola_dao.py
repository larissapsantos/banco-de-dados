from .conexao import criar_conexao

# CREATE 

def inserir_escola(nome, bairro=None, uf=None, ano_inauguracao=None):
    sql = """
    INSERT INTO escola (nome, bairro, uf, ano_inauguracao)
    VALUES (%s, %s, %s, %s)
    """

    try:
        conn = criar_conexao()
        if conn is None:
            return None

        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nome, bairro, uf, ano_inauguracao))
                novo_id = cur.lastrowid   # id gerado pelo auto_increment
        return novo_id

    except Exception as e:
        print("Erro ao inserir escola:", e)
        return None


# READ - Retorna uma lista de dicionários com todas as escolas

def listar_escolas():
    sql = """
        SELECT id, nome, bairro, uf, ano_inauguracao
        FROM escola
        ORDER BY id
    """

    try:
        conn = criar_conexao()
        if conn is None:
            return []

        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                resultados = cur.fetchall()   # lista de dicts
        return resultados

    except Exception as e:
        print("Erro ao listar escolas:", e)
        return []


# READ - Retorna um dicionário com os dados da escola ou None se não encontrar.


def buscar_escola_por_id(escola_id):
    sql = """
        SELECT id, nome, bairro, uf, ano_inauguracao
        FROM escola
        WHERE id = %s
    """

    try:
        conn = criar_conexao()
        if conn is None:
            return None

        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (escola_id,))
                resultado = cur.fetchone()   # um registro só
        return resultado

    except Exception as e:
        print("Erro ao buscar escola por id:", e)
        return None


# UPDATE - Atualiza TODOS os campos da escola com o id dado. Retorna True se atualizou alguma linha, False caso contrário.

def atualizar_escola(escola_id, nome, bairro, uf, ano_inauguracao):
    sql = """
        UPDATE escola
        SET nome = %s,
            bairro = %s,
            uf = %s,
            ano_inauguracao = %s
        WHERE id = %s
    """

    try:
        conn = criar_conexao()
        if conn is None:
            return False

        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (nome, bairro, uf, ano_inauguracao, escola_id))
                linhas = cur.rowcount
        return linhas > 0

    except Exception as e:
        print("Erro ao atualizar escola:", e)
        return False


# DELETE - Deleta a escola com o id dado. Retorna True se excluiu alguma linha, False caso contrário.

def deletar_escola(escola_id):
    sql = "DELETE FROM escola WHERE id = %s"

    try:
        conn = criar_conexao()
        if conn is None:
            return False

        with conn:
            with conn.cursor() as cur:
                cur.execute(sql, (escola_id,))
                linhas = cur.rowcount
        return linhas > 0

    except Exception as e:
        print("Erro ao deletar escola:", e)
        return False
