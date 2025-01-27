import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P08_CalculoDistancia.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_calcular_velocidad.clicked.connect(self.calcular_velocidad)


    #Area de los Slots
    def calcular_velocidad(self):
        try:
            distancia = float(self.txt_distancia.text())
            tiempo = float(self.txt_tiempo.text())
            if tiempo == 0:
                self.msj("El tiempo no puede ser cero.")
                return
            velocidad = distancia / tiempo
            self.msj(f"Velocidad: {velocidad:.2f} Km/h")
        except ValueError:
            self.msj("Por favor, ingresa valores válidos para distancia y tiempo.")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())