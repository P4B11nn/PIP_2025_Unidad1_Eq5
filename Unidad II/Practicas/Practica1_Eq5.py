import sys
from contextlib import nullcontext

from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "Practica1_Eq5.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.selectorImagen.setMinimum(1)
        self.selectorImagen.setMaximum(10)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(1) ##valr inicial
        self.selectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarioDatos = {
            1: ("../Archivos/image_5.jpg", ["Gato", "4 meses", "Raton"]),
            2: ("../Archivos/LOGOFACULTAD.png", ["Castor", "65 años", "Estudiar"]),
            3: ("../Archivos/LOGOUAT.png", ["Correcaminos", "75 años", "Superacion"]),
            4: ("../Archivos/image_1.jpg", ["Bryan C.", "60 años", "Meta"]),
            5: ("../Archivos/image_2.jpg", ["Kirby", "5 años", "Cualquier cosa"]),
            6: ("../Archivos/image_4.png", ["Billie Eilish", "21", "Musica"]),
            7: ("../Archivos/image_6.jpg", ["Spider-man", "22", "Venom"]),
            8: ("../Archivos/image_7.jpg", ["Musashi", "25", "Katana"]),
            9: ("../Archivos/image_8.jpg", ["Pintura", "11 meses", "Pincel"]),
            10: ("../Archivos/image_3.jpg", ["Thorfinn", "25", "Espada de madera"]),
        }
        self.indice = 1
        self.obtenerDatos()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.cambiaValorAutomatico)
        self.btn_iniciar.clicked.connect(self.iniciarTemporizador)
        self.btn_detener.clicked.connect(self.timer.stop)

    # Área de los Slots
    def obtenerDatos(self):
        nombre = self.diccionarioDatos[self.indice][1][0]
        edad = self.diccionarioDatos[self.indice][1][1]
        juguete = self.diccionarioDatos[self.indice][1][2]

        self.txt_nombre.setText(nombre)
        self.txt_edad.setText(edad)
        self.txt_juguete.setText(juguete)

        pixmap = QtGui.QPixmap(self.diccionarioDatos[self.indice][0])
        if pixmap.isNull():
            print(f"Error: No se pudo cargar la imagen {self.diccionarioDatos[self.indice][0]}")
        self.label_image.setPixmap(pixmap)

    def cambiaValor(self):
        self.indice = self.selectorImagen.value()
        self.obtenerDatos()

    def cambiaValorAutomatico(self):
        self.indice += 1
        if self.indice > self.selectorImagen.maximum():
            self.indice = self.selectorImagen.minimum()
        self.selectorImagen.setValue(self.indice)

    def iniciarTemporizador(self):
        try:
            interval_text = self.txt_intervalo.text()
            if not interval_text:
               print("Error: No se ha ingresado un intervalo")
               return
            interval = int(interval_text) * 1000
            if interval <= 0:
               print("Error: El intervalo debe ser mayor a 0")
               return

            self.timer.start(interval)
        except ValueError:
             print("Error: El intervalo debe ser un número entero")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

