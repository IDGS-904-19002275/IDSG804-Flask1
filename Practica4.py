from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/practica4', methods=['GET'])
def index():
  return render_template('practica4.html')


if __name__ == '__main__':
  app.run(debug=True, port=8000)