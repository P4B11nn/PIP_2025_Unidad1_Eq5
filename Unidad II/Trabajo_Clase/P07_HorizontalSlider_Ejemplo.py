import  sys
from PyQt5 import uic,QtWidgets


qtCreatorFile = "P07_HorizontalSlider_Ejemplo.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.HorizontalSlider.setMinimum(-50)
        self.HorizontalSlider.setMaximum(50)
        self.HorizontalSlider.setSingleStep(5)
        self.HorizontalSlider.setValue(-50)
        self.HorizontalSlider.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("-50")



    #Area de los Slots
    def cambiaValor(self):
        valor = self.HorizontalSlider.value()
        self.txt_valor.setText(str(valor))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

