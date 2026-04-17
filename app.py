from flask import Flask, render_template,redirect, request, session, flash
from model.produto import recuperar_produtos, recuperar_produtos_destaque, recup_produto
from model.usuario import Usuario

app = Flask(__name__)

@app.route("/")
def pg_inicial():
    produto = recuperar_produtos()
    destaque = recuperar_produtos_destaque()
    return render_template("index.html", produto = produto, destaque = destaque)


@app.route("/produto/<codigo>")
def pg_produto(codigo):
    prod = recup_produto(codigo)
    return render_template("produto.html", prod = prod)

@app.route("/cadastrar_usuario", methods=["POST"])
def cadastro():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get("nome")

    novo_usu = Usuario(usuario,senha,nome)
    novo_usu.cadastrar()

    return redirect("/")

@app.route("/cadastro_login")
def cadastro_login():
    return render_template("cadastro.html")




if (__name__) == "__main__":
    app.run(debug=True)
