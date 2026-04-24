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
	usuario VARCHAR(20) PRIMARY KEY,
    senha  VARCHAR(200) NOT NULL,
    nome VARCHAR(100) DEFAULT "ANONIMO"    
);

CREATE TABLE IF NOT EXISTS carrinho(
	cod_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(20),
    data DATETIME DEFAULT CURRENT_TIMESTAMP,
    finalizado BOOL,
    CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES cadastro(usuario)
);

CREATE TABLE IF NOT EXISTS item_carrinho(
	cod_item_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    cod_carrinho INT,
    cod_produto INT,
    quantidade INT DEFAULT 0,
    CONSTRAINT fk_item_carrinho FOREIGN KEY (cod_carrinho) REFERENCES carrinho(cod_carrinho),
    CONSTRAINT fk_item_carrinho_itens FOREIGN KEY (cod_produto) REFERENCES produto(codigo)
);

SELECT carrinho.cod_carrinho, carrinho.usuario, carrinho.data, carrinho.finalizado, produto.produtos, item_carrinho.quantidade, produto.preco, produto.url_imagem FROM carrinho
INNER JOIN item_carrinho ON carrinho.cod_carrinho = item_carrinho.cod_carrinho
INNER JOIN produto ON produto.codigo = item_carrinho.cod_produto
WHERE carrinho.usuario = "Camss";


