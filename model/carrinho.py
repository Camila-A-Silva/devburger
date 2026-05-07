from database.conexao import conectar

def recuperar_carrinho(usuario:str) -> list:
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT carrinho.cod_carrinho, carrinho.usuario, carrinho.data, carrinho.finalizado, produto.produtos, item_carrinho.quantidade, produto.preco, produto.url_imagem FROM carrinho
                    INNER JOIN item_carrinho ON carrinho.cod_carrinho = item_carrinho.cod_carrinho
                    INNER JOIN produto ON produto.codigo = item_carrinho.cod_produto
                    WHERE carrinho.usuario = %s;
                    """,[usuario])
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def inserir_item (usuario,cod_produto,quantidade=1):
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT cod_carrinho from carrinho
                    WHERE usuario = %s
                    AND finalizado = 0
                    LIMIT 1
                    """,[usuario])
    resultado_carrinho = cursor.fetchone()

    if resultado_carrinho:
        codigo_carrinho = resultado_carrinho["cod_carrinho"]
    else:
        cursor.execute("""
                        INSERT INTO carrinho (usuario)
                        VALUES (%s);
                        """,[usuario])
        codigo_carrinho = cursor.lastrowid
        
    cursor.execute("""
                    INSERT INTO item_carrinho
                            (cod_carrinho, cod_produto, quantidade)
                    VALUES (%s, %s, %s);
                    """,[codigo_carrinho, cod_produto, quantidade])
    
    conexao.commit()

    conexao.close()