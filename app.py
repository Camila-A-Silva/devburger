from flask import Flask, render_template
from model.produto import recuperar_produtos, recuperar_produtos_destaque, recup_produto

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

if (__name__) == "__main__":
    app.run(debug=True)
