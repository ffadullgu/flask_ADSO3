from flask import Flask
app=Flask(__name__)

@app.route('/')
def inicio():
    return "<h1> Primer Aplicación Web en entorno virtual </h1>"


@app.route('/registro')
def adicionar():

    return "<h1> Registrar Usuario </h1>"

@app.route('/consulta')
def consulta():
    return "<h1> Consultar </h1>"

@app.route('/fin')
def salir():
    return "<h1> Adios</h1>"