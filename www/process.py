from database import Database
from models import Samples

import random
import time
import signal
import sys

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True

"""main: Genera los parametros requeridos y 
los almacena en la base de datos
Parametros recibidos: session de la db
"""

def main(session):
    killer = GracefulKiller()
    while(1):
        #asignacion de parametros a los valores
        r = Samples(temperature=random.randint(10,13),humidity=random.randint(50,55),pressure=random.randint(1019,1022), windspeed=random.randint(20,40))

        #agregarlos a la sesion obtenida en el main principal
        session.add(r)

        #llevarlos a la db
        session.commit()
        print("Valores actualizados")
        time.sleep(1)
        if killer.kill_now:
            session.close()
            break

if __name__ == '__main__':   
    db = Database()
    session = db.get_session()
    main(session)
    