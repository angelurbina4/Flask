from crypt import methods
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "as678as75asd77sda9dncbnvbn665"

@app.route("/")
def home():
    if "count" not in session:
        session['count'] = 1
    elif "multipler" in session:
        session['count']  += int(session['multipler'])
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route("/masdos")
def masDos():
    if 'multipler' in session:
        session.pop("multipler")
        session['count'] += 1
    else:
        session['count'] += 1
    return redirect('/')

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

@app.route("/success", methods = ['POST']) 
def multiplier():
    print(request.form)
    session['multipler'] = request.form['quantity']
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


#pip3 install pipenv
#pipenv install flask
#python3 -m pipenv <command to use> SOLO SI RECIBIMOS ERROR
#pipenv shell
#python3 server.py