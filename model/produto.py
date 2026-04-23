from database.conexao import conectar

def recuperar_produtos():
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo, produtos, descricao, destaque, preco_ori, preco, url_imagem, disponibilidade from produto")

    produto = cursor.fetchall()
    conexao.close()
    return produto


def recuperar_produtos_destaque():
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo, produtos, url_imagem from produto WHERE destaque = 1")

    produto = cursor.fetchall()
    conexao.close()
    return produto

def recup_produto(codigo:int):
    conexao, cursor = conectar()
    cursor.execute("SELECT codigo, produtos, descricao, destaque, preco_ori, preco, url_imagem, disponibilidade from produto WHERE codigo = %s",[codigo])

    produto = cursor.fetchone()
    conexao.close()
    return produto