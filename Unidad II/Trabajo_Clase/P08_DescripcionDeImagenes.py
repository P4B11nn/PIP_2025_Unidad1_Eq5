import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_DescripcionDeImagenes.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.selectorImagen.setMinimum(0)
        self.selectorImagen.setMaximum(3)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(0) #valor inicial
        self.selectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarioDatos = {
            1: ("../Archivos/image_5.jpg",["Gato", "4 meses", "Raton"]),
            2: ("../Archivos/FIT_logo_vertical.png", ["Castor", "65 años", "Estudiar"]),
            3: ("../Archivos/LOGOUAT.png", ["Correcaminos", "75 años", "Superacion"])
        }
        self.indice = 1

        self.txt_nombre.setText("")
        self.txt_edad.setText("")
        self.txt_juguete.setText("")
        self.label.setPixmap(QtGui.QPixmap())

    # Área de los Slots
    def obtenerDatos(self):
        if self.indice == 0:
            self.txt_nombre.setText("")
            self.txt_edad.setText("")
            self.txt_juguete.setText("")
            self.label.setPixmap(QtGui.QPixmap())
        else:
            nombre = self.diccionarioDatos[self.indice][1][0]
            edad = self.diccionarioDatos[self.indice][1][1]
            juguete = self.diccionarioDatos[self.indice][1][2]
            self.txt_nombre.setText(nombre)
            self.txt_edad.setText(edad)
            self.txt_juguete.setText(juguete)

    def cambiaValor(self):
        self.indice = self.selectorImagen.value()
        self.obtenerDatos()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
