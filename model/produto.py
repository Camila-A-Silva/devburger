from database.conexao import conectar

def recuperar_produtos():
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo, produtos, descricao, destaque, preco, url_imagem, disponibilidade from produto")

    produto = cursor.fetchall()
    conexao.close()
    return produto


def recuperar_produtos_destaque():
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo, produtos, descricao, destaque, preco, url_imagem, disponibilidade from produto WHERE destaque = 1")

    produto = cursor.fetchall()
    conexao.close()
    return produto
