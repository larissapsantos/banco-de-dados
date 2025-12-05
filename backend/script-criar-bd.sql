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
    foto LONGBLOB,
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

CREATE TRIGGER trg_professor_foto_padrao
BEFORE INSERT ON professor
FOR EACH ROW
BEGIN
    IF NEW.foto IS NULL THEN
        SET NEW.foto = 0x89504e470d0a1a0a0000000d49484452000000100000001008060000001ff3ff61000000097048597300000ec400000ec401952b0e1b000002f54944415438cbad934d681c6500869f6fe69bd95f66dd75d7266e8d266d63376afa934deb612154c5a42d8278685c4aada8b58a27c18bd09b178f1e04316d55b44228148956d47a28a645690e89644b08695a8dc9d6dd7493ddec7f7676e6f32008556ffa1c5f5e9ed3fbc27f44fc3d38793036747ca4e3c4ee443825fddeb8303d38d2c8cedeac5dfdf4cba5d3ef7f36ffc33f045bac9efbb74613879f19349f18e8f38d5a212112dbca44ef73c0e361ad6e319f8d526d9a6a7ab638fec537f9cbcbbf5fff3abf76e3b6888713bdc9879e9bbab371dbd24d4d787c26fdc95e966f15191dae80d418ff3648f14e01290542c023bbb6ab5f6f54ca5373e7f7c9ced08ec36ba5bce5baae308424d611e6a943835c3877996b3301105058c9a149404aeedd12e6c0c8809858bf6275867b0f89c7e24fa623deed9f375b0d61f824a6d720140ed2acb77969b88cdda8f2e1c5084a38485347931ac1a01fbba154b690392ab3c5cc57fd7d7b1b8bb986bfbde98082c26689482846b2e716f5621e2bd04d613d8febb8e852a3d4acd01d0bb53a1f98fc5eaed757ab6fec9f333fb8b6935ca985ab5c829e20c7524b74459bb47c1ae97d19ceffb48b5aa38a8ea4336cf0e68b0bfaebef3aeb0220f7f690dd34d764261fa5e67a49f494e8db69a26b3e680b9ae5020b4b2d16573b08592e03c906d6d6a82df74f9812a0d5d4972356a4fbe9dd35b45099772e8458dcd018deaba00ddf5d8f90f9c5e554da41f825c21fc6deb4570024c0cc4af54a2a18e8f6f8bce87e9bd7461a9cb9e4e7dc2517803d3d1aaf1ed4d14d01029463333d5f9afc4b303e971b4b763d7c4c9a4a6886a2e39e36a7d275846efe59518010a029140ac776d4c7177f3b7dd79427d22367061f942f07ac1abe500bdd72113e85901a4ad30181120a47b94c2d54cea6de9a7de52e41cc1f303e7af6f9b13d5de671af7f5598c10a466013cde7200c1717816d1b6afa66fd9323effd7c32bfd1b2fff54c2ff41f181a7df4f113fdf168caf4d4e29a6ce0885636b3ba72757c263376f6c7b949fe4ffe009328289f6a4068840000000049454e44ae426082;
    END IF;
END


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
