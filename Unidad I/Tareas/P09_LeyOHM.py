import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P09_LeyOHM.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_calcular_voltaje.clicked.connect(self.calcular_voltaje)

    #Area de los Slots
    def calcular_voltaje(self):
        try:
            corriente = float(self.txt_corriente.text())
            resistencia = float(self.txt_resistencia.text())
            voltaje = corriente * resistencia
            self.msj(f"Voltaje: {voltaje:.2f} V")
        except ValueError:
            self.msj("Por favor, ingresa valores válidos para corriente y resistencia.")

    # Función para mostrar mensajes emergentes
    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())