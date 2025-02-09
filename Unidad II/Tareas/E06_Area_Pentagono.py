#Liz version
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E06_Area_pentagono.ui"  # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.Slider_perimetro.setMinimum(00)
        self.Slider_perimetro.setMaximum(1000)
        self.Slider_perimetro.setSingleStep(5)
        self.Slider_apotema.setMinimum(00)
        self.Slider_apotema.setMaximum(1000)
        self.Slider_apotema.setSingleStep(5)
        self.Slider_perimetro.valueChanged.connect(self.calcular_area)
        self.Slider_apotema.valueChanged.connect(self.calcular_area)

    # Area de los Slots

    def calcular_area(self):
            perimetro =  self.Slider_perimetro.value()
            apotema =  self.Slider_apotema.value()
            self.input_perimetro.setText(f"{perimetro}")
            self.input_apotema.setText(f"{apotema}")
            area = self.calcular_area_pentagono( perimetro, apotema)
            self.label_resultado_area.setText(f"{area:.2f}  m^2")

    def calcular_area_pentagono(self, perimetro, apotema):
        return  (perimetro * apotema) / 2



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



