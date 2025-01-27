import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P01_IMC.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcular_imc.clicked.connect(self.calcular_imc)

    def calcular_imc(self):
        try:

            peso = float(self.txt_peso.text())
            altura = float(self.txt_altura.text())

            if peso <= 0 or altura <= 0:
                self.msj("Por favor, ingresa valores positivos para el peso y la altura.")
                return

            imc = peso / (altura ** 2)

            if imc < 18.5:
                categoria = "Bajo peso"
            elif 18.5 <= imc < 24.9:
                categoria = "Peso normal"
            elif 25 <= imc < 29.9:
                categoria = "Sobrepeso"
            else:
                categoria = "Obesidad"

            self.msj(f"Tu IMC es: {imc:.2f}\nCategoría: {categoria}")

        except ValueError:
            self.msj("Por favor, ingresa valores numéricos válidos para el peso y la altura.")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())