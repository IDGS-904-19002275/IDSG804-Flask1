# Practica4_SignosZodiacales
from flask import Flask, request, render_template
import math
app = Flask(__name__)


@app.route("/zodiaco/",methods=['GET','POST'])
def zodiaco():
    if request.method=='POST':
        nom = str(request.form.get('nom'))
        apa = str(request.form.get('apa'))
        ama = str(request.form.get('ama'))

        dia = int(request.form.get('dia'))
        mes = int(request.form.get('mes'))
        anio = int(request.form.get('anio'))

        sex = request.form.get('sex')

        pregunta1 = int(request.form.get('pregunta1'))
        pregunta2 = int(request.form.get('pregunta2'))
        pregunta3 = int(request.form.get('pregunta3'))
        pregunta4 = int(request.form.get('pregunta4'))

        zodiac = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra","Mono", "Gallo", "Perro", "Cerdo"]
        animal =  zodiac[(anio - 4) % 12]

        calificacion = 0
        if pregunta1 == 2:
            calificacion += 2.5
        if pregunta2 == 3:
            calificacion += 2.5
        if pregunta3 == 2:
            calificacion += 2.5
        if pregunta4 == 1:
            calificacion += 2.5
        
        nombre = nom +' '+ apa +' '+ ama
        
        return render_template("practica4-signos.html",
                               n = nombre, a = animal, c= calificacion, e = (2022-anio))
    else:
        return render_template("practica4.html")


@app.route("/zodiaco2/",methods=['GET','POST'])
def otrozodiaco():
    return render_template("practica-signos.html",n = 'nombre', a = 'conejo', c= 8, e = (2022-2001))
if __name__ == '__main__':
    app.run(debug=True)