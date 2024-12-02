# CREATE DATABASE ESCOLA;
# -- PONTO E VIRGULA INDICA O FINAL DO COMANDO

# -- PARA SELECIONAR UM BANCO PARA MANIPULAR USAR O COMANDO 'USE'

# USE ESCOLA;

# -- TODA TABELA É PADÃO QUE TENHA UM ID --> IDENTIFICADOR
# -- criando uma tabela no meu banco de dados
# CREATE TABLE aluno(
# 	matricula INT PRIMARY KEY,
# 	nome VARCHAR(120),
#     idade INT,
#     data_nascimento DATE,
#     sobrenome VARCHAR(30)
# );

# CREATE TABLE professor(
# 	id INT PRIMARY KEY AUTO_INCREMENT,
#     nome VARCHAR(50),
#     data_nascimento DATE,
#     materia_id INT,
#     FOREIGN KEY (materia_id) REFERENCES materia(id)
# );
# CREATE TABLE materia(
# 	id INT PRIMARY KEY,
#     descrição VARCHAR(200)
# );
# -- EXCLUINDO A MINHA TABELA
# DROP TABLE aluno;
# INSERT INTO aluno (matricula,nome,idade,data_nascimento,sobrenome)
# VALUES (123456,'GIUZEPPI',45,'1972-06-02','Souto'
# );
# INSERT INTO professor (nome, data_nascimento, materia_id)
# VALUES ('João Silva', '1980-05-15', 1),
#        ('Maria Oliveira', '1975-10-22', 2),
#        ('Carlos Souza', '1990-03-30', 3);
# INSERT INTO materia (id, descrição)
# VALUES (1, 'Matemática'),
#        (2, 'Física'),
#        (3, 'Química');

# -- VISUALIZANDO MINHA TABELA aluno
# SELECT * FROM aluno;
# SELECT * FROM professor;
# SELECT * FROM materia;

