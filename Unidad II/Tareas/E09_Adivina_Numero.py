#Alex version
import sys
import random
from PyQt5 import uic,QtWidgets

qtCreatorFile = "E09_Adivina_Numero.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.horizontalSlider.setRange(1, 100)  # Valores de 1 a 100
        self.horizontalSlider.setValue(50)  #
        self.numero_secreto = random.randint(1, 100)
        self.horizontalSlider.valueChanged.connect(self.verificar_numero)
        self.btnReiniciar.clicked.connect(self.reiniciar_juego)
        self.verificar_numero()
   #Area de los Slots
    def verificar_numero(self):
        num = self.horizontalSlider.value()
        self.labelNumero.setText(f"Número elegido: {num}")  # Actualiza la etiqueta

        if num < self.numero_secreto:
            self.labelMensaje.setText("El número secreto es mayor")
        elif num > self.numero_secreto:
            self.labelMensaje.setText("El número secreto es menor")
        else:
            self.labelMensaje.setText("¡Correcto! Adivinaste el número 🎉")

    def reiniciar_juego(self):
        self.numero_secreto = random.randint(1, 100)  # Nuevo número aleatorio
        self.labelMensaje.setText("Intenta adivinar el nuevo número")  # Mensaje inicial
        self.horizontalSlider.setValue(50)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

