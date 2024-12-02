CREATE DATABASE projeto;

CREATE TABLE produto(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(255),
	descricao VARCHAR(255),
    quantidade INT,
    preço_unitario FLOAT,
    codigo_de_barras VARCHAR(255)
);
CREATE TABLE estoque(
    id_produto INT NOT NULL,
    nome_produto VARCHAR(255),
    descricao VARCHAR(255),
    quantidade INT,
    preço_unitario FLOAT,
    codigo_de_barra VARCHAR(255),
    FOREIGN KEY (id_produto, nome_produto, descricao, quantidade, preço_unitario, codigo_de_barra) REFERENCES produto(id, nome, descricao, quantidade, preço_unitario, codigo_de_barra)
);

CREATE TABLE vendas(
	id INT PRIMARY KEY AUTO_INCREMENT,
	quantidade INT,
    produto_id INT NOT NULL,
    nome_produto VARCHAR(80),
    FOREIGN KEY( produto_id, nome_produto ) REFERENCES produto(id, nome)
);
