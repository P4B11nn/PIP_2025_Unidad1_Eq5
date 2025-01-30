import sys
from PyQt5 import uic,QtWidgets


qtCreatorFile = "P05_Componente_Dial_Ejemplo.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.Dial.setMinimum(-50)
        self.Dial.setMaximum(50)
        self.Dial.setSingleStep(5)
        self.Dial.setValue(-50)
        self.Dial.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("-50")



    #Area de los Slots
    def cambiaValor(self):
        valor = self.Dial.value()
        self.txt_valor.setText(str(valor))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

