from flask import Flask
from flask import request
import math

app = Flask(__name__)

@app.route("/Tarea2/",methods=['GET','POST'])
def suma():
    if request.method=='POST':
        x1 = int(request.form.get('X1'))
        x2 = int(request.form.get('X2'))

        y1 = int(request.form.get('Y1'))
        y2 = int(request.form.get('Y2'))
        
        horiz = int(X2 - X1)
        vert = int(Y2 - Y1)
        dis = math.sqrt( horiz**2 + vert**2 )

        return '<h2>La distancia es de:{}</h2>'.format(str(dis))
    else:
        return '''
            <form action='/Tarea2/' method='POST'>

            <label>Coordenadas primer punto</label>
            <label>X</label>
            <input type='text' name='X1'/>

            <label>Y</label>
            <input type='text' name='Y1'/>
            <br><br>

            <label>Coordenadas segundo punto</label>
            <label>X</label>
            <input type='text' name='X2'/>
            <label>Y</label>
            <input type='text' name='Y2'/>

            <input type='submit' value='Calcular distancia'/>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)