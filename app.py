from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pg_inicial():
    return render_template("index.html")

@app.route("/hamburguer_1")
def pg_h1():
    return render_template("h1.html")

@app.route("/hamburguer_2")
def pg_h2():
    return render_template("h2.html")

@app.route("/hamburguer_3")
def pg_h3():
    return render_template("h3.html")

@app.route("/hamburguer_4")
def pg_h4():
    return render_template("h4.html")

@app.route("/hamburguer_5")
def pg_h5():
    return render_template("h5.html")

@app.route("/hamburguer_6")
def pg_h6():
    return render_template("h6.html")





if (__name__) == "__main__":
    app.run(debug=True)
