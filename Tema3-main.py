from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return 'Hola'

#pasar un string
@app.route("/user/<string:user>")
def user(user):
    return 'Hola '+user+' Aqui dice hola'

#pasar un int
@app.route("/num/<int:i>")
def num(i):
    return 'Tu calificacion es: {}'.format(i)

#pasar 
@app.route("/suma/<float:a>/<float:b>")
def suma(a,b):
    return 'La suma es: {}'.format(a+b)




#pasar varios parametros
@app.route("/users/<int:i>/<string:u>")
def users(i,u):
    return '{} esta de {} de 10'.format(u,i)




if __name__ == '__main__':
   
    app.run(debug=True)
