from flask import Flask, render_template,redirect, request, session, flash
from model.produto import recuperar_produtos, recuperar_produtos_destaque, recup_produto
from model.cadastro import cadastro, verificar_usuario

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


@app.route("/cadastro")
def pg_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=["POST"])
def rota_cad():
    login = request.form.get("login")
    senha = request.form.get("senha")
    cadastro(login, senha)
    return redirect("/cadastro")


@app.route("/login")
def pg_login():
    if "usuario_logado" in session:
        return redirect("/admin")
    session.clear()
    return render_template("login.html")
    

@app.route("/login", methods=["POST"])
def rota_log():
    login = request.form.get("usuario")
    senha = request.form.get("senha") 
    usuario = verificar_usuario(login, senha)
    session.clear()

    if usuario:
        session["nome"] = usuario
        return redirect("/admin")
    else:
        flash("Usuário ou senha inválida!","danger")
        return redirect("/login")
    
@app.route("/logoff")
def logoff():
    session.clear()
    return redirect("/login")


if (__name__) == "__main__":
    app.run(debug=True)
