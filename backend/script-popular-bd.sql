use projetoBD;

INSERT INTO escola (nome, bairro, uf, ano_inauguracao) VALUES
('Escola Classe 101', 'Ceilândia', 'DF', 1985),
('Escola Classe 102', 'Taguatinga', 'DF', 1990),
('Escola Classe 103', 'Sobradinho', 'DF', 1988),
('Escola Classe 104', 'Gama', 'DF', 1992),
('Escola Classe 105', 'Planaltina', 'DF', 1987),
('Escola Classe 106', 'Brazlândia', 'DF', 1995),
('Escola Classe 107', 'Recanto das Emas', 'DF', 2000),
('Escola Classe 108', 'Samambaia', 'DF', 1998),
('Escola Classe 109', 'Santa Maria', 'DF', 1991),
('Escola Classe 110', 'São Sebastião', 'DF', 1989),
('Escola Classe 111', 'Ceilândia', 'DF', 1993),
('Escola Classe 112', 'Taguatinga', 'DF', 1996),
('Escola Classe 113', 'Sobradinho', 'DF', 2001),
('Escola Classe 114', 'Gama', 'DF', 1986),
('Escola Classe 115', 'Planaltina', 'DF', 1994),
('Escola Classe 116', 'Brazlândia', 'DF', 2002),
('Escola Classe 117', 'Recanto das Emas', 'DF', 1997),
('Escola Classe 118', 'Samambaia', 'DF', 1988),
('Escola Classe 119', 'Santa Maria', 'DF', 2000),
('Escola Classe 120', 'São Sebastião', 'DF', 1999);


INSERT INTO professor (matricula, nome, situacao, id_escola) VALUES
(2013, 'Ana Silva', 'ativo', 1),
(2765, 'Bruno Souza', 'inativo', 2),
(2481, 'Carla Oliveira', 'ativo', 3),
(2934, 'Daniel Lima', 'ativo', 4),
(2547, 'Eduarda Costa', 'inativo', 5),
(2820, 'Felipe Rocha', 'ativo', 6),
(2198, 'Gabriela Martins', 'inativo', 7),
(2604, 'Hugo Fernandes', 'ativo', 8),
(2751, 'Isabela Pereira', 'ativo', 9),
(2237, 'João Santos', 'inativo', 10),
(2859, 'Karen Almeida', 'ativo', 11),
(2643, 'Lucas Ribeiro', 'inativo', 12),
(2991, 'Mariana Gomes', 'ativo', 13),
(2375, 'Nicolas Costa', 'ativo', 14),
(2543, 'Olivia Carvalho', 'inativo', 15),
(2728, 'Pedro Barbosa', 'ativo', 16),
(2617, 'Quésia Fernandes', 'inativo', 17),
(2094, 'Rafael Lima', 'ativo', 18),
(2842, 'Sofia Mendes', 'ativo', 19),
(2930, 'Tiago Alves', 'inativo', 20),
(2156, 'Vanessa Nunes', 'ativo', 1),
(2279, 'William Silva', 'inativo', 2),
(2623, 'Xavier Rocha', 'ativo', 3),
(2781, 'Yasmin Oliveira', 'ativo', 4),
(2309, 'Zeca Costa', 'inativo', 5),
(2540, 'Alice Martins', 'ativo', 6),
(2867, 'Bruna Fernandes', 'ativo', 7),
(2952, 'Caio Pereira', 'inativo', 8),
(2204, 'Diana Santos', 'ativo', 9),
(2685, 'Enzo Almeida', 'ativo', 10),
(2971, 'Fabiana Ribeiro', 'inativo', 11),
(2128, 'Gustavo Gomes', 'ativo', 12),
(2637, 'Helena Costa', 'ativo', 13),
(2794, 'Igor Carvalho', 'inativo', 14),
(2153, 'Juliana Barbosa', 'ativo', 15),
(2916, 'Karina Fernandes', 'ativo', 16),
(2462, 'Leonardo Lima', 'inativo', 17),
(2850, 'Michele Mendes', 'ativo', 18),
(2097, 'Natan Alves', 'ativo', 19),
(2748, 'Olga Nunes', 'inativo', 20);

INSERT INTO coordenador (matricula, nome, situacao, id_escola) VALUES
(50123, 'Beatriz Almeida', 'ativo', 1),
(52765, 'Caio Souza', 'inativo', 2),
(54812, 'Diana Pereira', 'ativo', 3),
(59341, 'Eduardo Lima', 'ativo', 4),
(55472, 'Fernanda Costa', 'inativo', 5),
(58204, 'Gustavo Rocha', 'ativo', 6),
(51987, 'Helena Martins', 'inativo', 7),
(56043, 'Igor Fernandes', 'ativo', 8),
(57512, 'Júlia Oliveira', 'ativo', 9),
(52376, 'Leonardo Santos', 'inativo', 10),
(58591, 'Marcela Almeida', 'ativo', 11),
(56432, 'Natan Ribeiro', 'ativo', 12),
(59912, 'Olívia Gomes', 'ativo', 13),
(53752, 'Paulo Costa', 'ativo', 14),
(55431, 'Renata Carvalho', 'inativo', 15),
(57284, 'Samuel Barbosa', 'ativo', 16),
(56179, 'Tânia Fernandes', 'inativo', 17),
(50941, 'Vinícius Lima', 'ativo', 18),
(58423, 'Yara Mendes', 'ativo', 19),
(59304, 'Zé Alves', 'inativo', 20),
(51563, 'Amanda Nunes', 'ativo', 1),
(52791, 'Bruno Silva', 'inativo', 2),
(56234, 'Carolina Rocha', 'ativo', 3),
(57812, 'Diego Oliveira', 'ativo', 4),
(53092, 'Elaine Costa', 'inativo', 5),
(55408, 'Fabio Martins', 'ativo', 6),
(58675, 'Gabriela Fernandes', 'ativo', 7),
(59527, 'Hugo Pereira', 'inativo', 8),
(52049, 'Isabela Santos', 'ativo', 9),
(56851, 'João Almeida', 'ativo', 10);

INSERT INTO administrador (matricula, nome, email, bairro, uf) VALUES
(90123, 'Ana Beatriz Almeida', 'anabeatrizalmeida@educacao.gov.br', 'Asa Norte', 'DF'),
(90234, 'Bruno Costa', 'brunocosta@educacao.gov.br', 'Asa Sul', 'DF'),
(90345, 'Carla Mendes', 'carlamendes@educacao.gov.br', 'Taguatinga', 'DF'),
(90456, 'Daniel Oliveira', 'danieloliveira@educacao.gov.br', 'Ceilândia', 'DF'),
(90567, 'Eliana Rocha', 'elianarocha@educacao.gov.br', 'Samambaia', 'DF'),
(90678, 'Felipe Lima', 'felipelima@educacao.gov.br', 'Planaltina', 'DF'),
(90789, 'Gabriela Nunes', 'gabrielanunes@educacao.gov.br', 'Sobradinho', 'DF'),
(90890, 'Henrique Santos', 'henriquesantos@educacao.gov.br', 'Gama', 'DF'),
(90912, 'Isabela Ferreira', 'isabelaferreira@educacao.gov.br', 'Riacho Fundo', 'DF'),
(91023, 'João da Cunha', 'joaodacunha@educacao.gov.br', 'Santa Maria', 'DF');

INSERT INTO categoria (nome, descricao) VALUES 
('Robótica', 'Kits, placas, sensores e componentes eletrônicos'),
('Impressão 3D', 'Impressoras e filamentos'),
('Ferramentas', 'Ferramentas manuais, elétricas e equipamentos de bancada');

INSERT INTO fabricante (cnpj, nome, bairro, uf, telefone) VALUES 
('11111111000111', 'RoboCore', 'São Paulo', 'SP', '1199999999'),
('22222222000122', 'Creality', 'Shenzhen', 'CN', '0000000000'),
('33333333000133', 'Arduino Org', 'Monza', 'IT', '0000000000'),
('44444444000144', 'Bosch', 'Campinas', 'SP', '1933333333'),
('55555555000155', 'Stanley', 'São Paulo', 'SP', '1144444444'),
('66666666000166', 'Prusa Research', 'Praga', 'CZ', '0000000000'),
('77777777000177', 'Raspberry Pi Fdn', 'Cambridge', 'UK', '0000000000');

INSERT INTO equipamento (nome, descricao, localizacao, condicao, status, id_fabricante, id_categoria, data_compra) VALUES 
('Kit Arduino Uno', 'Kit iniciante com placa R3 e sensores básicos', 'Armário A', 'Novo', 'Disponível', '11111111000111', 1, '2024-01-10'),
('Impressora Ender 3', 'Impressora 3D FDM de entrada', 'Bancada 2', 'Bom', 'Disponível', '22222222000122', 2, '2023-11-15'),
('Kit LEGO Mindstorms', 'Robótica educacional EV3', 'Armário B', 'Usado', 'Disponível', '11111111000111', 1, '2022-05-20'),
('Notebook Dell', 'Inspiron 15 para programação', 'Carrinho 1', 'Bom', 'Disponível', '11111111000111', 1, '2023-02-10');

-- ROBÓTICA
INSERT INTO equipamento (nome, descricao, localizacao, condicao, data_compra, status, id_fabricante, id_categoria) VALUES 
('Placa Raspberry Pi 4', 'Modelo B com 4GB de RAM', 'Armário A - Prateleira 2', 'Novo', '2024-01-15', 'Disponível', '77777777000177', 1),
('Kit Sensor Ultrassônico', 'Pacote com 10 sensores HC-SR04', 'Gaveta E1', 'Bom', '2023-11-20', 'Disponível', '33333333000133', 1),
('Motor DC com Roda', 'Kit motor + roda para carrinho robô', 'Gaveta E2', 'Novo', '2024-02-10', 'Disponível', '11111111000111', 1),
('Microbit V2', 'Placa educativa para programação em blocos', 'Armário A - Prateleira 1', 'Excelente', '2024-03-05', 'Disponível', '77777777000177', 1),
('Kit Arduino Mega', 'Placa Mega 2560 com cabo USB', 'Armário A - Prateleira 3', 'Usado', '2022-08-15', 'Manutenção', '33333333000133', 1),
('Protoboard 830 Furos', 'Placa de ensaio grande', 'Gaveta E3', 'Bom', '2023-05-10', 'Disponível', '11111111000111', 1);

-- IMPRESSÃO 3D
INSERT INTO equipamento (nome, descricao, localizacao, condicao, data_compra, status, id_fabricante, id_categoria) VALUES 
('Impressora Prusa i3 MK3', 'Impressora 3D de alta precisão', 'Bancada 3', 'Excelente', '2023-12-01', 'Disponível', '66666666000166', 2),
('Filamento PLA Branco', 'Rolo de 1kg - 1.75mm', 'Armário B - Estoque', 'Novo', '2024-04-01', 'Disponível', '22222222000122', 2),
('Filamento ABS Preto', 'Rolo de 1kg - 1.75mm (Requer mesa aquecida)', 'Armário B - Estoque', 'Novo', '2024-04-01', 'Disponível', '22222222000122', 2),
('Resina UV Cinza', 'Garrafa de 500ml para impressora SLA', 'Armário Químico', 'Novo', '2024-02-20', 'Disponível', '22222222000122', 2),
('Bico Extrusor 0.4mm', 'Kit reposição para Ender 3', 'Caixa de Ferramentas 3D', 'Novo', '2023-10-10', 'Disponível', '22222222000122', 2);

-- FERRAMENTAS
INSERT INTO equipamento (nome, descricao, localizacao, condicao, data_compra, status, id_fabricante, id_categoria) VALUES 
('Parafusadeira Bosch', 'Bateria 12V com kit de bits', 'Painel de Ferramentas', 'Bom', '2023-01-15', 'Emprestado', '44444444000144', 3),
('Jogo de Chaves de Fenda', 'Kit com 6 chaves (fenda e philips)', 'Caixa F1', 'Usado', '2022-05-20', 'Disponível', '55555555000155', 3),
('Alicate de Corte', 'Alicate diagonal para eletrônica', 'Caixa F2', 'Bom', '2023-06-15', 'Disponível', '55555555000155', 3),
('Ferro de Solda', '60W com suporte', 'Bancada Eletrônica', 'Bom', '2023-09-01', 'Disponível', '11111111000111', 3),
('Multímetro Digital', 'Mede tensão, corrente e resistência', 'Bancada Eletrônica', 'Novo', '2024-01-20', 'Disponível', '11111111000111', 3),
('Serra Tico-Tico', 'Serra elétrica para madeira e metal', 'Armário Inferior', 'Bom', '2022-11-30', 'Disponível', '44444444000144', 3);

INSERT INTO equipamento (nome, descricao, localizacao, condicao, data_compra, status, id_fabricante, id_categoria) VALUES 
('Kit Arduino Uno', 'Kit extra para aulas grandes', 'Armário A - Prateleira 4', 'Novo', '2024-05-10', 'Disponível', '11111111000111', 1),
('Kit Arduino Uno', 'Kit extra para aulas grandes', 'Armário A - Prateleira 4', 'Novo', '2024-05-10', 'Disponível', '11111111000111', 1),
('Kit Arduino Uno', 'Kit extra para aulas grandes', 'Armário A - Prateleira 4', 'Novo', '2024-05-10', 'Disponível', '11111111000111', 1),
('Kit Arduino Uno', 'Kit extra para aulas grandes', 'Armário A - Prateleira 4', 'Novo', '2024-05-10', 'Disponível', '11111111000111', 1),
('Kit Arduino Uno', 'Kit extra para aulas grandes', 'Armário A - Prateleira 4', 'Novo', '2024-05-10', 'Disponível', '11111111000111', 1),
('Kit Arduino Uno', 'Kit extra para aulas grandes', 'Armário A - Prateleira 4', 'Novo', '2024-05-10', 'Disponível', '11111111000111', 1),
('Kit Arduino Uno', 'Kit extra para aulas grandes', 'Armário A - Prateleira 4', 'Novo', '2024-05-10', 'Disponível', '11111111000111', 1),
('Kit Arduino Uno', 'Kit extra para aulas grandes', 'Armário A - Prateleira 4', 'Novo', '2024-05-10', 'Disponível', '11111111000111', 1),
('Kit Arduino Uno', 'Kit extra para aulas grandes', 'Armário A - Prateleira 4', 'Novo', '2024-05-10', 'Disponível', '11111111000111', 1),
('Kit Arduino Uno', 'Kit extra para aulas grandes', 'Armário A - Prateleira 4', 'Novo', '2024-05-10', 'Disponível', '11111111000111', 1);