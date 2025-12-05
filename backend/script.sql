CREATE DATABASE projetoBD;

USE projetoBD;

CREATE TABLE escola (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    bairro VARCHAR(100),
    uf CHAR(2),
    ano_inauguracao YEAR
);

CREATE TABLE coordenador (
    matricula INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    situacao VARCHAR(50),
    id_escola INT NOT NULL,
    FOREIGN KEY (id_escola) REFERENCES escola(id)
);

CREATE TABLE professor (
    matricula INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    situacao VARCHAR(50),
    id_escola INT NOT NULL,
    FOREIGN KEY (id_escola) REFERENCES escola(id)
);

CREATE TABLE administrador (
    matricula INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    bairro VARCHAR(100),
    uf CHAR(2)
);

CREATE TABLE fabricante (
cnpj CHAR(14) PRIMARY KEY,
nome VARCHAR(100),
telefone CHAR(11),
bairro VARCHAR(100),
uf CHAR(2)
);

CREATE TABLE categoria (
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100),
descricao VARCHAR (300)
);

CREATE TABLE equipamento (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(300),
    localizacao VARCHAR(100),
    condicao VARCHAR(50),
    data_compra DATE,
    status VARCHAR(50),
    id_fabricante CHAR(14) NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_fabricante) REFERENCES fabricante(cnpj),
    FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);


CREATE TABLE plano_aula (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    descricao VARCHAR(500),
    status VARCHAR(50),
    id_professor INT NOT NULL,
    id_coordenador INT NOT NULL,
    FOREIGN KEY (id_professor) REFERENCES professor(matricula),
    FOREIGN KEY (id_coordenador) REFERENCES coordenador(matricula)
);

CREATE TABLE emprestimo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    data_hora DATETIME NOT NULL,
    id_escola INT NOT NULL,
    id_equipamento INT NOT NULL,
    id_plano_aula INT NOT NULL,
    FOREIGN KEY (id_escola) REFERENCES escola(id),
    FOREIGN KEY (id_equipamento) REFERENCES equipamento(id),
    FOREIGN KEY (id_plano_aula) REFERENCES plano_aula(id)
);

CREATE TABLE solicitacao (
    id_servidor INT,
    id_emprestimo INT,
    id_coordenador INT,
    status VARCHAR(50),
    PRIMARY KEY (id_servidor, id_emprestimo, id_coordenador),
    FOREIGN KEY (id_servidor) REFERENCES administrador(matricula),
    FOREIGN KEY (id_emprestimo) REFERENCES emprestimo(id),
    FOREIGN KEY (id_coordenador) REFERENCES coordenador(matricula)
);

CREATE TABLE historico_emprestimo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_emprestimo INT,
    data_hora_emprestimo DATETIME,
    status VARCHAR(50),
    FOREIGN KEY (id_emprestimo) REFERENCES emprestimo(id)
);

CREATE TRIGGER trg_registrar_historico_emprestimo
AFTER INSERT ON emprestimo
FOR EACH ROW
BEGIN
    DECLARE status_equipamento VARCHAR(50);

    UPDATE equipamento SET status = 'Emprestado' WHERE id = NEW.id_equipamento;

    SELECT status 
    INTO status_equipamento 
    FROM equipamento 
    WHERE id = NEW.id_equipamento;

    INSERT INTO historico_emprestimo (
        id_emprestimo,
        data_hora_emprestimo,
        status
    ) VALUES (
        NEW.id,
        NOW(),
        status_equipamento
    );
END;


CREATE PROCEDURE sp_criar_solicitacao(
    IN p_id_servidor INT,
    IN p_id_emprestimo INT,
    IN p_id_coordenador INT
)
BEGIN
    INSERT INTO solicitacao (
        id_servidor,
        id_emprestimo,
        id_coordenador,
        status
    ) VALUES (
        p_id_servidor,
        p_id_emprestimo,
        p_id_coordenador,
        'Em Análise' -- Valor Fixo Para Criação
    );
    
    SELECT * FROM solicitacao 
    WHERE id_servidor = p_id_servidor 
      AND id_emprestimo = p_id_emprestimo
      AND id_coordenador = p_id_coordenador;
END;

CREATE VIEW vw_plano_aula_com_professor AS
SELECT 
    p.*,
    prof.nome AS nome_professor,
    e.bairro AS bairro_escola,
    e.nome AS nome_escola
FROM plano_aula p
JOIN professor prof ON prof.matricula = p.id_professor
JOIN escola e ON e.id = prof.id_escola
WHERE p.status <> 'APROVADO'
ORDER BY p.id;
