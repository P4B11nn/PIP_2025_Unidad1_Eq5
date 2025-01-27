import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P05_AreaRectangulo.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_calcular_AreaRec.clicked.connect(self.area_rectangulo)


    #Area de los Slots
    def area_rectangulo(self):
        try:
            base = float(self.txt_base_rectangulo.text())
            altura = float(self.txt_altura_rectangulo.text())
            area = base * altura
            self.msj(f"Área: {area:.2f} m^2")
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
