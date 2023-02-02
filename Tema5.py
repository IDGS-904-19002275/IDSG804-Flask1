#estructura general del un proyeto de flask
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")#ruta de acceso de la api, y el tipo de request
def index():
    return render_template("index.html")

@app.route("/alumnos")#ruta de acceso de la api, y el tipo de request
def alumnos():
    return render_template("alumnos.html")


@app.route("/usuarios")#ruta de acceso de la api, y el tipo de request
def usuarios():
    return render_template("usuarios.html")




if __name__=="__main__":
    app.run(debug=True,port=3000)