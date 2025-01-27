import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P03_PuntoMedio.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_calcular_punto.clicked.connect(self.punto_medio)



    #Area de los Slots
    def punto_medio(self):
        try:
            x1 = float(self.txt_x1.text())
            y1 = float(self.txt_y1.text())
            x2 = float(self.txt_x2.text())
            y2 = float(self.txt_y2.text())
            xm = (x1 + x2) / 2
            ym = (y1 + y2) / 2

            self.msj(f"Punto medio: ({xm:.2f}, {ym:.2f})")

        except ValueError:
            self.msj("Por favor, ingresa valores numéricos válidos.")

    def msj(self, txt):
            m = QtWidgets.QMessageBox()
            m.setText(txt)
            m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
