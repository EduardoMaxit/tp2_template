import os
import signal
import subprocess


class Process(object):
    process = None

    """start_process: Iniciar proceso
    si no hay otro proceso iniciado
    
    Retorno:
        Devuelve el pid (id del proceso) si el proceso comienza correctamente / None si hay un proceso iniciado antes
    """

    def start_process(self):
        if self.process == None:
            #se inicia el proceso. Llamado al main principal del proceso sin parametros. No necesario pasaje de parametros
            cmd = "python process.py"
            self.process = subprocess.Popen(cmd.split(), preexec_fn=os.setsid)
            return self.process.pid
        return None
    
    """is_running: Determina si el proceso se esta ejecutando
        Retorno: Devuelve True si se esta ejecutando, False en caso contrario

    """
    def is_running(self):
        return self.process != None

    """stop_process: Matar el proceso si se esta ejecutando
    """

    def stop_process(self):
        if self.process != None:
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            self.process = None
