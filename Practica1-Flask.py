from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/ops/",methods=['GET','POST'])
def suma():
    if request.method=='POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        res = 0
        if(request.form.get('res') == 'Suma'):
            res = num1 + num2
        if(request.form.get('res') == 'Resta'):
            res = num1 - num2
        if(request.form.get('res') == 'Multiplicacion'):
            res = num1 * num2
        if(request.form.get('res') == 'Division'):
            res = num1 / num2

        return '<h2>El resultado es:{}</h2>'.format(str(int(res)))
    else:
        return '''
            <form action='/ops' method='POST'>
            <input type='radio' name='res' value='Suma' required checked    > Suma <br>
            <input type='radio' name='res' value='Resta'> Resta <br>
            <input type='radio' name='res' value='Mumtiplicacion'> Multiplicar <br>
            <input type='radio' name='res' value='Division'> Divicion <br>
            <label>N1: </label>
            <input type='text' name='num1'/>
            <br><br>
            <label>N2: </label>
            <input type='text' name='num2'/>
            <br><br>
            <input type='submit' value='Calcular'/>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)