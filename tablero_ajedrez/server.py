from tkinter.tix import COLUMN
from flask  import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tablero_ajedrez():
    return render_template("index.html", column=8, fila=8, color1='red', color2='blue')

@app.route('/<int:fila>')
def tablero_ajedrez2(fila):
    return render_template("index.html", column=8, fila=fila, color1='red', color2='blue')

@app.route('/<int:fila>/<int:column>')
def tablero_ajedrez3(fila, column):
    return render_template("index.html", fila=fila, column=column, color1='red', color2='blue')

@app.route('/<int:fila>/<int:column>/<string:color1>')
def tablero_ajedrez4(fila, column, color1):
    return render_template("index.html", fila=fila, column=column, color1=color1, color2='blue')

@app.route('/<int:fila>/<int:column>/<string:color1>/<string:color2>')
def tablero_ajedrez5(fila, column, color1, color2):
    return render_template("index.html", fila=fila, column=column, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)