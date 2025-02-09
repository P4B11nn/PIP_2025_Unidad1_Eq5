# Jesus falzo version
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E01_Celsius_a_Fahrenheit.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        self.horizontalSlider.setMinimum(-100)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)


        self.horizontalSlider.valueChanged.connect(self.cambiaValor)


        self.txt_valor.setText("0")
        self.txt_valor_2.setText("32")

    def cambiaValor(self):
        celsius = self.horizontalSlider.value()

        fahrenheit = (celsius * 9 / 5) + 32

        self.txt_valor.setText(str(celsius))
        self.txt_valor_2.setText(f"{fahrenheit:.2f}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
