# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo flask
# la clase request permite acceso a la información de la petición HTTP
from flask import Flask, request, jsonify    

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template

from Usuario import Usuario
import ControladorUsuarios

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

# decorator: se usa para indicar el URL Path por el que se va a invocar nuestra función
@app.route('/')      
def hello():
    return 'Hola Mundo Web!'
  
# los parametros en la URL llegan en request.args 
@app.route('/params')      
def params():
    return request.args;

# Retorna un objeto como JSON
@app.route('/usuario')      
def usuario():
    try:
        usuario_buscado = ControladorUsuarios.BuscarPorCedula( request.args["cedula"] )
        return jsonify(usuario_buscado)
    except Exception as err:
        # Retorna el mensaje de error de la excepcion como una cadena
        return { "status": "error", "mensaje": "La peticion no se puede completar", "error": str(err) } 

    
# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run( debug=True )