from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('/index.html')

@app.route('/fin')
def salir():
    return "<h1> Adios</h1>"