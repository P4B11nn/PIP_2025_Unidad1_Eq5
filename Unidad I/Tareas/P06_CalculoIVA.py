import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P06_CalculoIVA.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_calcularIVA.clicked.connect(self.calcular_iva)


    #Area de los Slots
    def calcular_iva(self):
        try:
            cantidad = float(self.txt_cantidad.text())
            porcentaje_iva = float(self.txt_porcentaje_iva.text()) * 0.01
            iva = cantidad * porcentaje_iva
            total = cantidad + iva
            self.msj(f"IVA: {iva:.2f}, Total: {total:.2f}")
        except ValueError:
            self.msj("Por favor, ingresa una cantidad válida.")

    def msj(self, txt):
     m = QtWidgets.QMessageBox()
     m.setText(txt)
     m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
