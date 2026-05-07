from flask import Flask, render_template,redirect, request, session, flash, jsonify
from model.produto import recuperar_produtos, recuperar_produtos_destaque, recup_produto
from model.usuario import Usuario
from model.carrinho import recuperar_carrinho, inserir_item

app = Flask(__name__)
app.secret_key = "azul"

@app.route("/")
def pg_inicial():
    produto = recuperar_produtos()
    destaque = recuperar_produtos_destaque()
    return render_template("index.html", produto = produto, destaque = destaque)


@app.route("/produto/<codigo>")
def pg_produto(codigo):
    prod = recup_produto(codigo)
    return render_template("produto.html", prod = prod)

@app.route("/cadastro")
def pg_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar_usuario", methods=["POST"])
def cadastro():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get("nome")

    novo_usu = Usuario(usuario,senha,nome)
    novo_usu.cadastrar()

    return redirect("/login")

@app.route("/login")
def pg_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def logar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    usuario_log = Usuario.logar(usuario, senha)

    if usuario_log:
        session ["usuario_logado"] = usuario_log 

    return redirect("/")

@app.route("/api/get/carrinho", methods=["GET"])
def api_get_carrinho():
    if "usuario_logado" in session:
        carrinho = recuperar_carrinho(session["usuario_logado"]["usuario"])
        return jsonify(carrinho), 200
    else:
        return jsonify({"message":"Usuário não logado"}), 401
    

@app.route("/api/post/item_carrinho", methods=["POST"])
def api_post_item_carrinho():
    if "usuario_logado" in session:
        usuario = session["usuario_logado"]["usuario"]
        dados_json = request.get_json()
        cod_produto = dados_json.get("cod_produto")
        quantidade = dados_json.get("quantidade")

        inserir_item(usuario, cod_produto, quantidade)
        return jsonify({"message":"Inserido com sucesso"}), 200

    else:
        return redirect("/login")





if (__name__) == "__main__":
    app.run(debug=True)
