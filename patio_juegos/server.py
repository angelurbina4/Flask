from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Welcome!</h1>"

@app.route('/play')
def play():
    return render_template("index.html", color="lightblue", num=3)

@app.route('/play/<int:num>')
def play2(num):
    return render_template("index.html", color ="lightblue", num=num)

@app.route('/play/<int:num>/<string:color>')
def play(num, color):
    return render_template("index.html", color =color, num=num)

if __name__ == "__main__":
    app.run(debug=True)