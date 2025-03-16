import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E07_Teorema_Pitagoras.ui"  # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.Slider_cateto1.setMinimum(00)
        self.Slider_cateto1.setMaximum(1000)
        self.Slider_cateto1.setSingleStep(10)
        self.Slider_cateto2.setMinimum(00)
        self.Slider_cateto2.setMaximum(1000)
        self.Slider_cateto2.setSingleStep(10)
        self.Slider_cateto1.valueChanged.connect(self.calcular)
        self.Slider_cateto2.valueChanged.connect(self.calcular)

    # Area de los Slots

    def calcular(self):
            cateto1 =  self.Slider_cateto1.value()
            cateto2 =  self.Slider_cateto2.value()
            self.input_cateto1.setText(f"{cateto1}")
            self.input_cateto2.setText(f"{cateto2}")
            hipotenusa = self.calcular_hipotenusa( cateto1, cateto2)
            self.label_resultado.setText(f"{hipotenusa:.2f}  m")


    def calcular_hipotenusa(self, cateto1, cateto2):
      return  (cateto1 ** 2 + cateto2 ** 2) ** 0.5



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



