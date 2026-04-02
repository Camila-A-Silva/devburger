CREATE DATABASE IF NOT EXISTS db_hamburguer;

USE db_hamburguer;

CREATE TABLE IF NOT EXISTS produto(
	codigo INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(30),
    descricao VARCHAR(300),
    destaque BOOL,
    preco FLOAT,
    url_imagem VARCHAR(200)
);
