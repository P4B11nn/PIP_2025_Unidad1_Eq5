#Mi verion
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E05_Peso_a_USD.ui"  # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.slider_pesos.setMinimum(00)
        self.slider_pesos.setMaximum(10000)
        self.slider_pesos.setSingleStep(1)
        self.slider_pesos.setValue(0)
        self.slider_pesos.valueChanged.connect(self.conversion_monedas)
        self.txt_pesos.setText("0")
        self.txt_USD.setText("0.0")
        self.slider_pesos.valueChanged.connect(self.conversion_monedas)

    # Area de los Slots
    def conversion_monedas(self):
        pesos = self.slider_pesos.value()
        dolares = pesos / 20
        self.txt_pesos.setText(f"{pesos} pesos")
        self.txt_USD.setText(f"{dolares:.2f} dólares")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())