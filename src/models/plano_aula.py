class PlanoAula:
    def __init__(self, id_plano_aula, titulo, descricao, status, id_professor):
        self.id_plano_aula = id_plano_aula
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.id_professor = id_professor

    def to_dict(self):
        return {
            "id_plano_aula": self.id_plano_aula,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "id_professor": self.id_professor
        }

    @classmethod
    def from_dict(cls, dicionario):
        return cls(
            id_plano_aula = dicionario.get("id_plano_aula"),
            titulo = dicionario.get("titulo"),
            descricao = dicionario.get("descricao"),
            status = dicionario.get("status"),
            id_professor = dicionario.get("id_professor")
        )