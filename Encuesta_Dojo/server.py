from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "L4 $uP3r 1nCr318l3 c0ntR4$3#4"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=['POST', 'GET'])
def process():
    print(request.form)
    
    session['nombre'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['message'] = request.form['message']
    
    return redirect('/results')

@app.route("/results")
def results():
        
    return render_template("results.html")


if (__name__) == "__main__":
    app.run(debug=True)