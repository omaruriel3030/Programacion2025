import threading
import time
from Temporizador_1 import Temporizador

class Semaforo():
    def __init__(self):
        print ('Dentro de semaforo')

        self.TON_0= Temporizador('TON_00',12)
        self.TON_1= Temporizador('TON_01',0.8)
        self.TON_2= Temporizador('TON_02',0.3)
        self.TON_3= Temporizador('TON_03',10)
        self.TON_4= Temporizador('TON_04',1) 
        self.TON_5= Temporizador('TON_05',2)
        self.M0 = True
        self.luz_roja=False
        self.luz_amarilla= False
        self.luz_verde= False
        self.luz_azul= False
        self.luz_naranja = False
        self.luz_negra = False
        

        self.worker=None


        self.tarea=threading.Thread(target=self.semaforo_funcionando)

    def iniciar(self):
        if self.tarea:
            self.tarea.start()

    def semaforo_funcionando(self):
        while True:
            
            self.TON_0.entrada=self.M0 and not self.TON_3.salida
            self.TON_0.actualizar()
            self.TON_1.entrada=self.M0 and self.TON_0.salida #bien
            self.TON_1.actualizar()
            self.TON_2.entrada=self.M0 and self.TON_1.salida #bien
            self.TON_2.actualizar()
            self.TON_3.entrada=self.M0 and self.TON_2.salida 
            self.TON_3.actualizar()
            self.TON_4.entrada=self.M0 and self.TON_5.salida 
            self.TON_4.actualizar()
            self.TON_5.entrada=self.M0 and not self.TON_4.salida 
            self.TON_5.actualizar()
            
            self.luz_roja=self.M0 and not self.TON_0.salida
            self.luz_amarilla=self.M0 and self.TON_0.salida and not self.TON_1.salida #duda
            self.luz_verde=self.M0 and  self.TON_1.salida
            self.luz_azul=self.M0 and not self.TON_5.salida  

            print(f'R:{self.luz_roja} A: {self.luz_amarilla} V:{self.luz_verde} AZ: {self.luz_azul} \
                  B1:{self.luz_naranja} B2: {self.luz_negra}')

            #mapeando hacia la interfaz
            if self.worker:
                self.worker.prender_luz_roja(self.luz_roja)

            if self.worker:
                self.worker.prender_luz_amarillo(self.luz_amarilla)

            if self.worker:
                self.worker.prender_luz_verde(self.luz_verde)

            if self.worker: 
                self.worker.prender_luz_azul(self.luz_azul)

            
            time.sleep(0.01)

    def establecer_worker(self, worker):
        self.worker =worker
def main():
    print("Dentro de main")
    semaforo = Semaforo()
    semaforo.iniciar()

if __name__ =="__main__":
    main()