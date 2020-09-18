from flask import Flask, request
from pathlib import Path
import json


app = Flask(__name__)

@app.route('/ordenar',methods=['GET'])
def ordenar():
    arrayArgs = list(request.args.keys())
    response = sorted(arrayArgs)

    return json.dumps(response)

@app.route('/contarMayusculas',methods=['GET'])
def contarMayusculas():
    response = ""
    cantidad = 0
    ruta = request.args.get('ruta', '')
    if ruta == "":
        response = "Debe ingresar una ruta"
    else:
        fileName = ruta
        fileObj = Path(fileName)
        try:
            archivo = open(ruta, "r")
            for linea in archivo.readlines():
                cantidad += contarMayusEnString(linea)
            archivo.close()
            response = "El archivo tiene {} mayusculas".format(cantidad)
        except FileNotFoundError as e:
            response = "El archivo no existe"         
    return json.dumps(response)


def contarMayusEnString(cadena):
    cantidad = 0 
    for letra in cadena:
        if letra.isupper():
            cantidad += 1
    return cantidad

if __name__ == '__main__':
    app.run(debug = True, host='localhost')