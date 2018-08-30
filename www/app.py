# Imports
from aux_pro import Process
from database import Database
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from models import Samples

import random
import time
import signal
import sys
  
app = Flask(__name__)
pro = Process()
db = Database()

"""@app.route "crea" una asociacion entre la url dada como
argumento y la funcion"""

# Definir la ruta para ingresar en el navegador
@app.route('/')
def index():
    #Si el proceso no esta corriendo se lo inicia, en caso contrario no tiene sentido
    if not (pro.is_running()):
    	pro.start_process()
    #Retorno del index.html definido
    return render_template('index.html')

#Obtencion de valores para actualizar parametros
@app.route('/valores', methods = ["GET"])
def get_valores():
	#Se obtienen los valores
    valores = db.get_valores()
    #Retorno de los valores hacia el script
    return jsonify({"temperatura":valores[0] ,"humedad":valores[1], "presatm":valores[2],"velviento":valores[3],"lasttemperatura":valores[4],"lasthumedad":valores[5],"lastpresatm":valores[6],"lastvelviento":valores[7]}) 


if __name__ == "__main__":
    # Define HOST and port
    app.run(host='0.0.0.0', port=8888)

