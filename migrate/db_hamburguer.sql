CREATE DATABASE IF NOT EXISTS db_hamburguer;

USE db_hamburguer;

CREATE TABLE IF NOT EXISTS produto(
	codigo INT AUTO_INCREMENT PRIMARY KEY,
    produtos  VARCHAR(30),
    descricao VARCHAR(300),
    destaque BOOL,
    preco VARCHAR(5),
    preco_ori VARCHAR(5),
    url_imagem VARCHAR(200),
    disponibilidade bool
);


CREATE TABLE IF NOT EXISTS cadastro(
	usuario VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(20),
    senha  VARCHAR(200)
);