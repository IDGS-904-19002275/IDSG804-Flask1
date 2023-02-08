from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        buyers = request.form['buyers']
        tickets = request.form['tickets']
        payment_method = request.form['payment_method']

        # aquí puedes procesar la información y hacer lo que quieras con ella

        return 'Información recibida: Nombre: {}, Compradores: {}, Boletos: {}, Tarjeta: {}'.format(
            name, buyers, tickets, payment_method
        )

    return '''
        <form action="/" method="post">
          <div class="form-group">
            <label for="name">Nombre:</label>
            <input type="text" class="form-control" id="name" name="name">
          </div>
          <div class="form-group">
            <label for="buyers">Cantidad de Compradores:</label>
            <input>
        '''