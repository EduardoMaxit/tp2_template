from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Samples

import os

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "samples"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()
    
    def get_session(self):
        """Singleton of db connection

        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session
    
    def get_valores(self):

        #Se obtiene la sesion
        session = self.get_session()

        #ultimos 10 valores. Orden por id (ultimo con id mas alto)
        #Con esto se pide devolucion de los ultimos 10 parametros, se los ordena por id en forma descendente 
        #(primer elemento = ultimo elemento ingresado), y se pide que lo devuelva como una lista)
        datos = session.query(Samples).order_by(Samples.id.desc()).limit(10).all()
        
        #se cierra la sesion
        session.close()

        #arreglo auxiliar
        parametros=[0,0,0,0,0,0,0,0]
        

        #control por si no existen aun datos en la db
        if(len(datos)!=0):
           
            #Se obtienen los valores acumulados
            for result in datos:
                parametros[0] += result.temperature
                parametros[1] += result.humidity
                parametros[2] += result.pressure
                parametros[3] += result.windspeed

            #Se obtienen los ultimos parametros
            parametros[4]=datos[0].temperature
            parametros[5]=datos[0].humidity
            parametros[6]=datos[0].pressure
            parametros[7]=datos[0].windspeed


            #Se realiza el promedio. Se obtiene valor promedio con un solo digito decimal
            for t in range(0,4):     
                parametros[t] = round(parametros[t]/len(datos), 1)
        
        return parametros

    