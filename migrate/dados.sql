INSERT INTO `db_hamburguer`.`produto`
(`produtos`,
`descricao`,
`destaque`,
`preco`,
`preco_ori`,
`url_imagem`,
`disponibilidade`)
VALUES
("Classic Dev",
"Pão brioche, carne suculenta e queijo derretido.",
"1",
"25,00",
"32,90",
"https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600",
"1"
),
("Double Stack",
"Dois hambúrgueres, bacon crocante e molho especial.",
"1",
"38,00",
"45,90",
"https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=600",
"1"
),
("Veggie Script",
"Hambúrguer de grão de bico com salada fresca.",
"1",
"30,00",
"35,00",
"https://images.pexels.com/photos/3219483/pexels-photo-3219483.jpeg?auto=compress&cs=tinysrgb&w=600",
"1"
),
("Java Chicken",
"Frango empanado crocante com alface e maionese.",
"1",
"28,00",
"34,90",
"https://images.pexels.com/photos/12034622/pexels-photo-12034622.jpeg",
"1"),
("Python Onion",
"Anéis de cebola, barbecue e queijo cheddar.",
"1",
"33,00",
"39,90",
"https://images.pexels.com/photos/70497/pexels-photo-70497.jpeg?auto=compress&cs=tinysrgb&w=600",
"1"),
("React Salad",
"Uma opção leve e reativa para o seu almoço.",
"1",
"27,00",
"31,50",
"https://images.pexels.com/photos/1199957/pexels-photo-1199957.jpeg?auto=compress&cs=tinysrgb&w=600",
"1");


INSERT INTO `db_hamburguer`.`cadastro` (`usuario`, `senha`, `nome`) VALUES ('Camss', '123', 'Camila');
INSERT INTO `db_hamburguer`.`cadastro` (`usuario`, `senha`, `nome`) VALUES ('Lena', '1234', 'Helena');

INSERT INTO `db_hamburguer`.`carrinho` (`usuario`, `finalizado`) VALUES ('Camss', '0');

INSERT INTO `db_hamburguer`.`item_carrinho` (`cod_carrinho`, `cod_produto`, `quantidade`) VALUES ('1','2', '2');
INSERT INTO `db_hamburguer`.`item_carrinho` (`cod_carrinho`, `cod_produto`, `quantidade`) VALUES ('1','5', '1');
INSERT INTO `db_hamburguer`.`item_carrinho` (`cod_carrinho`, `cod_produto`, `quantidade`) VALUES ('1','4', '1');



