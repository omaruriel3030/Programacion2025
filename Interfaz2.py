from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout,QHBoxLayout,\
QVBoxLayout, QRadioButton
import sys
from PyQt6.QtCore import QRunnable,QThreadPool,pyqtSignal as Signal, QObject,Qt

class Caja(QLabel):
    def __init__ (self,color):
        super().__init__()
        self.setStyleSheet(f'background-color:{color}')

class WorkerSignals(QObject):
    luz_roja = Signal(bool)
    luz_amarillo = Signal(bool)
    luz_verde = Signal(bool)
    luz_azul = Signal(bool)
    luz_naranja = Signal(bool)
    luz_negro = Signal(bool)
    
    def __init__(self):
        super().__init__()
       
class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    def prender_luz_roja(self, estado:bool = False):
        try: 
            self.signals.luz_roja.emit(estado)
        except Exception as e:
            print('Se obtuvo un error al emitir la señal')

    def prender_luz_amarillo(self, estado:bool = False):
        try: 
            self.signals.luz_amarillo.emit(estado)
        except Exception as e:
            print('Se obtuvo un error al emitir la señal')
    
    def prender_luz_verde(self, estado:bool = False):
        try: 
            self.signals.luz_verde.emit(estado)
        except Exception as e:
            print('Se obtuvo un error al emitir la señal')
            
    def prender_luz_azul(self, estado:bool = False):
        try: 
            self.signals.luz_azul.emit(estado)
        except Exception as e:
            print('Se obtuvo un error al emitir la señal')
            
    def prender_luz_naranja(self, estado:bool = False):
        try: 
            self.signals.luz_naranja.emit(estado)
        except Exception as e:
            print('Se obtuvo un error al emitir la señal')
            
    def prender_luz_negro(self, estado:bool = False):
        try: 
            self.signals.luz_negro.emit(estado)
        except Exception as e:
            print('Se obtuvo un error al emitir la señal')

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        contenedor0 = QGridLayout()
        contenedor1 = QGridLayout()

        widget = QWidget()
        main_layout = QHBoxLayout()
        
        layout_izquierdo = QVBoxLayout()
        self.indicador_naranja = self.crear_indicador('orange')
        self.indicador_negro = self.crear_indicador('black')
        layout_izquierdo.addWidget(self.indicador_naranja)
        layout_izquierdo.addWidget(self.indicador_negro)
        
        layout_derecho = QVBoxLayout()
        self.indicador_rojo = self.crear_indicador('red')
        self.indicador_amarillo = self.crear_indicador('yellow')
        self.indicador_verde = self.crear_indicador('green')
        self.indicador_azul = self.crear_indicador('blue')
        layout_derecho.addWidget(self.indicador_rojo)
        layout_derecho.addWidget(self.indicador_amarillo)
        layout_derecho.addWidget(self.indicador_verde)
        layout_derecho.addWidget(self.indicador_azul)
        
        main_layout.addLayout(layout_izquierdo)
        main_layout.addLayout(layout_derecho)
        
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.setWindowTitle('Semaforo')
        self.resize(350, 250)
        
        # Enlazando con el worker
        self.threadPool = QThreadPool()
        self.worker = Worker()
        self.worker.signals.luz_roja.connect(self.cambiar_indicador_rojo)
        self.worker.signals.luz_amarillo.connect(self.cambiar_indicador_amarillo)
        self.worker.signals.luz_verde.connect(self.cambiar_indicador_verde)
        self.worker.signals.luz_azul.connect(self.cambiar_indicador_azul)
        self.worker.signals.luz_naranja.connect(self.cambiar_indicador_naranja)
        self.worker.signals.luz_negro.connect(self.cambiar_indicador_negro)

    def cambiar_indicador_rojo(self, estado:bool):
        self.modificar_indicador(self.indicador_rojo, 'red' if estado else 'gray')

    def cambiar_indicador_amarillo(self, estado:bool):
        self.modificar_indicador(self.indicador_amarillo, 'yellow' if estado else 'gray')

    def cambiar_indicador_verde(self, estado:bool):
        self.modificar_indicador(self.indicador_verde, 'green' if estado else 'gray')

    def cambiar_indicador_azul(self, estado:bool):
        self.modificar_indicador(self.indicador_azul, 'blue' if estado else 'gray')
        
    def cambiar_indicador_naranja(self, estado:bool):
        self.modificar_indicador(self.indicador_naranja, 'orange' if estado else 'gray')
        
    def cambiar_indicador_negro(self, estado:bool):
        self.modificar_indicador(self.indicador_negro, 'black' if estado else 'gray')

    def modificar_indicador(self, indicador, color):
        indicador.setStyleSheet(f'background-color:{color}; border-radius:30')

    def crear_indicador(self, color:str = 'gray'):
        mi_caja = QLabel()
        mi_caja.setStyleSheet(f'background-color:{color}; border-radius:30')
        mi_caja.setFixedSize(60, 60)
        return mi_caja

    def obtener_worker(self):
        return self.worker

def main():
    print('dentro de main')
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()