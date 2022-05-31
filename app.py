from flask import Flask, render_template, request
from sympy import *

app = Flask(__name__)
init_printing(use_unicode=True)
x, y = symbols('x y')


@app.route('/')
def home():  # put application's code here
    print('request')
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index():
    var1 = request.form['first_inp']
    n = request.form['degree']
    deriv = Derivative(var1, x, n)
    deriv = deriv.doit()
    fxsimple = simplify(deriv)


    return render_template("index.html", der1=deriv, N=n, simplefx=fxsimple)


if __name__ == '__main__':
    app.run()
