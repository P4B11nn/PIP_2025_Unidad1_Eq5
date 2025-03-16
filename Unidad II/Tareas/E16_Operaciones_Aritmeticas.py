import sys
import random
from PyQt5 import QtWidgets, QtCore, uic

# Cargar la interfaz desde el archivo .ui
qtCreatorFile = "E16_Operaciones_Aritmeticas.ui"  # Asegúrate de que el nombre es correcto
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MathGame(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botones
        self.botonIniciar.clicked.connect(self.iniciar_juego)
        self.botonEnviar.clicked.connect(self.verificar_respuesta)

        # Configurar temporizador
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.control_tiempo)
        self.tiempo_restante = 0

        # Contadores
        self.correctas = 0
        self.total_preguntas = 0

        # Variables de la operación actual
        self.operando1 = 0
        self.operando2 = 0
        self.operador = ""
        self.resultado_correcto = 0

        print("Juego cargado correctamente.")

    def iniciar_juego(self):
        """Inicia el juego y el temporizador."""
        try:
            self.tiempo_restante = int(self.entrada_tiempo.text())
        except ValueError:
            self.mostrar_mensaje("Error", "Ingrese un número válido para el tiempo.")
            return

        if self.tiempo_restante <= 0:
            self.mostrar_mensaje("Error", "El tiempo debe ser mayor a 0.")
            return

        self.timer.start(1000)
        self.botonIniciar.setEnabled(False)
        self.generar_operacion()

    def control_tiempo(self):
        """Maneja la cuenta regresiva del temporizador."""
        self.tiempo_restante -= 1
        self.etiqueta_tiempo.setText(str(self.tiempo_restante))

        if self.tiempo_restante <= 0:
            self.timer.stop()
            self.finalizar_juego()

    def generar_operacion(self):
        """Genera una nueva operación matemática aleatoria."""
        self.operando1 = random.randint(1, 10)
        self.operando2 = random.randint(1, 10)
        self.operador = random.choice(["+", "-", "*", "/"])

        if self.operador == "/":
            self.operando1 = self.operando2 * random.randint(1, 5)  # Asegurar división exacta

        expresion = f"{self.operando1} {self.operador} {self.operando2}"
        self.resultado_correcto = eval(expresion)
        self.etiqueta_pregunta.setText(expresion)

    def verificar_respuesta(self):
        respuesta_usuario = self.entrada_respuesta.text().strip()

        if respuesta_usuario == str(self.resultado_correcto):
            self.lbl_estado.setText("Correcto ✔️")
            self.lbl_estado.setStyleSheet("color: green; font-size: 16px;")
            self.correctas += 1
        else:
            self.lbl_estado.setText("Incorrecto ❌")
            self.lbl_estado.setStyleSheet("color: red; font-size: 16px;")

        self.total_preguntas += 1
        self.generar_operacion()  # Generar nueva pregunta
        self.entrada_respuesta.clear()

    def finalizar_juego(self):
        """Muestra el resultado final y reinicia el juego."""
        mensaje = f"Respuestas correctas: {self.correctas} de {self.total_preguntas}"
        self.mostrar_mensaje("Tiempo terminado", mensaje)
        self.botonIniciar.setEnabled(True)
        self.correctas = 0
        self.total_preguntas = 0

    def mostrar_mensaje(self, titulo, mensaje):
        """Muestra un cuadro de diálogo con un mensaje."""
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MathGame()
    window.show()
    sys.exit(app.exec_())

