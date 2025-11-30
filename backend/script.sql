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
    FOREIGN KEY (id_professor) REFERENCES professor(matricula)
);

CREATE TABLE emprestimo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    quantidade INT,
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