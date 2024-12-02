# CREATE DATABASE ESCOLA;
# -- PONTO E VIRGULA INDICA O FINAL DO COMANDO

# USE ESCOLA;
# -- PARA SELECIONAR UM BANCO PARA MANIPULAR USAR O COMANDO 'USE'

# -- TODA TABELA É PADÃO QUE TENHA UM ID --> IDENTIFICADOR
# -- criando uma tabela no meu banco de dados
# CREATE TABLE aluno(
# 	id INT PRIMARY KEY AUTO_INCREMENT,
# 	nome VARCHAR(120),
#     data_nascimento DATE,
#     numero_matricula CHAR(8) UNIQUE,
#     curso_id INT NOT NULL,
#     FOREIGN KEY (curso_id) REFERENCES curso(id)
# );

# CREATE TABLE professor(
# 	id INT PRIMARY KEY AUTO_INCREMENT,
#     nome VARCHAR(50),
#     data_nascimento DATE,
#     materia_id INT,
#     FOREIGN KEY (materia_id) REFERENCES materia(id)
# );
# CREATE TABLE materia(
# 	id INT PRIMARY KEY AUTO_INCREMENT,
#     descrição TEXT(120),
#     curso_id INT NOT NULL,
#     FOREIGN KEY(curso_id) REFERENCES curso(id)
# );
# CREATE TABLE curso(
# 	id INT PRIMARY KEY AUTO_INCREMENT,
#     nome VARCHAR(80),
#     descrição TEXT(240)
# );
# -- EXCLUINDO A MINHA TABELA
# DROP TABLE aluno;
# DROP TABLE materia;
# DROP TABLE professor;
# DROP TABLE curso;
# -- Inserir 10 alunos
# INSERT INTO aluno (nome, data_nascimento, numero_matricula, curso_id) VALUES 
# ('Ana Silva', '2001-04-15', '20240001', 1),
# ('João Pereira', '2002-09-23', '20240002', 2),
# ('Maria Oliveira', '2000-12-01', '20240003', 1),
# ('Pedro Santos', '2001-07-19', '20240004', 3),
# ('Carla Costa', '2003-05-30', '20240005', 2), 
# ('Lucas Almeida', '2002-11-12', '20240006', 1),
# ('Fernanda Souza', '2001-01-22', '20240007', 3),
# ('Rafael Lima', '2004-08-09', '20240008', 2),
# ('Juliana Fernandes', '2002-03-25', '20240009', 1),
# ('Gustavo Martins', '2003-10-10', '20240010', 3);
# INSERT INTO professor (nome, data_nascimento, materia_id)
# VALUES ('João Silva', '1980-05-15', 1),
#        ('Maria Oliveira', '1975-10-22', 2),
#        ('Carlos Souza', '1990-03-30', 3);
# INSERT INTO materia (descrição,curso_id)
# VALUES ('Python',1),
#        ('SQL',2),
#        ('Estratégias de Marketing Global
# ',3),
#        ('Engenharia de Dados',2),
#        ('Logica de Programação',1);
# INSERT INTO curso (nome,descrição)
# VALUES("FULL STACK","CURSO PARA APRENDER A PROGRAMAR"),
# ('DATASCIENCE',"CURSO DE DATASCIENCE"),
# ('MARKETING',"CURSO DE MARKETING");
	
# -- VISUALIZANDO MINHAS TABELAS
# SELECT nome FROM aluno;
# SELECT * FROM professor;
# SELECT descrição FROM materia;
# SELECT nome FROM curso;
# SELECT * FROM aluno WHERE curso_id =1;
# SELECT nome as nome_do_aluno FROM aluno WHERE nome LIKE '%a%'; -- consulta o nome com tem a letra 'a'
# SELECT nome as nome_do_aluno FROM aluno WHERE nome LIKE 'a%'; -- consulta o nome que começa com a letra 'a'
# SELECT * FROM aluno WHERE id = 6;
# UPDATE aluno SET nome = 'Andre Oiveira' WHERE id = 6;

# SELECT 
# 	aluno.nome, 
# 	aluno.numero_matricula, 
# 	curso.nome 
# FROM
# 	aluno 
# INNER JOIN 
# 	curso 
# ON 
# 	aluno.curso_id = curso.id
# WHERE
# 	aluno.id = 4
# ;
