import random
import sys
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QPixmap

qtCreatorFile = "E10_Piedra_Papel_Tijeras.ui"  # Nombre del archivo UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botones
        self.btn_temporizar.clicked.connect(self.iniciar_juego)
        self.btn_Piedra.clicked.connect(lambda: self.seleccionar_opcion("piedra"))
        self.btn_Papel.clicked.connect(lambda: self.seleccionar_opcion("papel"))
        self.btn_Tijeras.clicked.connect(lambda: self.seleccionar_opcion("tijeras"))

        # Configurar temporizador
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control_tiempo)
        self.tiempo_restante = 10

        # Contadores de victorias
        self.victorias_jugador = 0
        self.victorias_pc = 0

        # Opciones del juego
        self.opciones = ["piedra", "papel", "tijeras"]
        self.eleccion_usuario = None

        print("Juego inicializado correctamente")

    def iniciar_juego(self):
        """Inicia el juego y el temporizador."""
        print("Juego iniciado")
        self.tiempo_restante = 10
        self.txt_temporizador.setText(str(self.tiempo_restante))
        self.eleccion_usuario = None
        self.segundoPlano.start(1000)
        self.btn_temporizar.setText("Jugando...")
        print(f"Temporizador iniciado con {self.tiempo_restante} segundos")

    def control_tiempo(self):
        """Controla la cuenta regresiva del temporizador."""
        self.tiempo_restante -= 1
        self.txt_temporizador.setText(str(self.tiempo_restante))
        print(f"Tiempo restante: {self.tiempo_restante}")

        if self.tiempo_restante == 0:
            self.segundoPlano.stop()
            print("Tiempo terminado")
            if not self.eleccion_usuario:
                print("No se eligió ninguna opción, seleccionando 'piedra' por defecto")
                self.eleccion_usuario = "piedra"
            self.jugar()
            self.mostrar_resultados()

    def seleccionar_opcion(self, opcion):
        """Registra la elección del usuario."""
        self.eleccion_usuario = opcion
        print(f"Opción seleccionada por el usuario: {self.eleccion_usuario}")
        self.jugar()

    def jugar(self):
        """Lógica del juego y selección de la máquina."""
        if not self.eleccion_usuario:
            print("Sin elección del usuario, no se puede jugar")
            return

        eleccion_pc = random.choice(self.opciones)
        print(f"Opción seleccionada por la máquina: {eleccion_pc}")

        # Mostrar imágenes según selección
        try:
            print(f"Cargando imagen de usuario: ../Archivos/{self.eleccion_usuario}.png")
            self.ImagenDeUsuario.setPixmap(QPixmap(f"../Archivos/{self.eleccion_usuario}.png"))

            print(f"Cargando imagen de PC: ../Archivos/{eleccion_pc}_flipped.png")
            self.ImagenDePc.setPixmap(QPixmap(f"../Archivos/{eleccion_pc}_flipped.png"))
        except Exception as e:
            print(f"Error cargando imágenes: {e}")

        # Determinar el ganador
        if self.eleccion_usuario == eleccion_pc:
            resultado = "Empate"
        elif (self.eleccion_usuario == "piedra" and eleccion_pc == "tijeras") or \
             (self.eleccion_usuario == "papel" and eleccion_pc == "piedra") or \
             (self.eleccion_usuario == "tijeras" and eleccion_pc == "papel"):
            resultado = "¡Ganaste!"
            self.victorias_jugador += 1
        else:
            resultado = "Perdiste"
            self.victorias_pc += 1

        print(f"Resultado: {resultado}")
        self.Ganador.setText(resultado)

    def mostrar_resultados(self):
        """Muestra los resultados en un QMessageBox y cambia el botón."""
        mensaje = f"Jugador: {self.victorias_jugador} victorias\nPC: {self.victorias_pc} victorias"
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Resultado Final")
        msg.setText(mensaje)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStyleSheet("color: red; font-size: 18px;")
        msg.exec_()

        # Cambiar el texto del botón a "Volver a JUGAR?"
        self.btn_temporizar.setText("JUGAR?")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
