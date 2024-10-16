#Importamos Flask
from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)


#Definimos una ruta principal
@app.route("/")
def HolaFlask():
    return "<h1>!Hola Flask !</h1> <hr>"

##Ahora tomamos la segunda ruta y la reemplazamos por el siguiete ejemplo 1.) Haga un programa que calcule el promedio de nostas sabiendo que tiene un valor de 30%, 30% y 40% respectivamente.
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=4,nota2=4,nota3=3):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*30)/100
    return f"<h1>El resultado es: {resultado}</h1><hr>"

##Tomamos la tercera ruta y la reemplazamos por el siguiente ejemplo 2) un programa que alcapturar la edad de la persona diga si es menor de edad < 18, un adulto mayor => 18 a 60, mayor >60,
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad<18:
        R="menor de edad"
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto mayor"
    return f"<h1>La persona es: {R}</h1> <hr>"

##Creamos otra ruta realizamos el siguiente ejemplo 3) Programa que crea arreglos con valores aleatorios 
##Importamos la libreria  numpy si no existe la instalamos con: pip install numpy
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=4,columnas=4,filas=4):
    if filas ==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo =np.random.randint(valores, size=(filas,columnas))
        
    return f"<h1>El arreglo aleatorio es: {arreglo} </h1> <hr>"
if __name__=='__main__':
    #El valor true indica que la app se deja en modo debug
    app.run(debug=True)