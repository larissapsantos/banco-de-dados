class Escola:
    def __init__(self, id_escola, nome, bairro, uf, ano_inauguracao):
        self.id_escola = id_escola
        self.nome = nome
        self.bairro = bairro
        self.uf = uf
        self.ano_inauguracao = ano_inauguracao
    
    def to_dict(self):  # trasformando objeto pra dicionario, metodo do objeto
        return{
            "id_escola": self.id_escola,
            "nome": self.nome,
            "bairro": self.bairro,
            "uf": self.uf,
            "ano_inauguracao": self.ano_inauguracao
        }
    
    @classmethod   # transformando dicionario pra objeto, metodo da classe
    def from_dict(cls, dicionario):
        return cls(
            id_escola = dicionario.get("id_escola"),
            nome = dicionario.get("nome"),
            bairro = dicionario.get("bairro"),
            uf = dicionario.get("uf"),
            ano_inauguracao = dicionario.get("ano_inauguracao")
        )