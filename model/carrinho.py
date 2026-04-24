from database.conexao import conectar

def recuperar_carrinho(usuario:str) -> list:
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT carrinho.cod_carrinho, carrinho.usuario, carrinho.data, carrinho.finalizado, produto.produtos, item_carrinho.quantidade, produto.preco, produto.url_imagem FROM carrinho
                    INNER JOIN item_carrinho ON carrinho.cod_carrinho = item_carrinho.cod_carrinho
                    INNER JOIN produto ON produto.codigo = item_carrinho.cod_produto
                    WHERE carrinho.usuario = "Camss";
                    """)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado