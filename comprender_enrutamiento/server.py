from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "<h1>¡Hola Mundo!</h1>"

@app.route('/dojo')
def dojo():
    return "<h2>¡Dojo!</h2>"

@app.route('/say/<string:name>')
def hola_name(name):
    return f"Hola {name}"

@app.route('/repeat/<int:num>/<string:name>')
def repeat_name(num, name):
    output = ''
    for i in range(0, num):
        output += '<p>'+name+'</p>'
    return output



if __name__ == "__main__":
    app.run(debug=True)


#pip3 install pipenv
#pipenv install flask
#python3 -m pipenv <command to use> SOLO SI RECIBIMOS ERROR
#pipenv shell
#python3 server.py