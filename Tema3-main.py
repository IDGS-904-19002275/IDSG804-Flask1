from flask import Flask
app = Flask (__name__)

@app.route("/")
def index():
    return'que pedo qleros '

#pasar un string
@app.route("/user/<string:user>")
def user(user):
    return'Hola  perros'+user

#pasar un int 
@app.route("/numero/<int:n>")
def user(n):
    return'numero: {}'.format(n)

if __name__=='__main__':
    app.run(debug=True)
