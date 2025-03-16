import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P00_Intro.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.cb_dormir.clicked.connect(self.control)
        self.cb_cine.toggled.connect(self.control)



    #Area de los Slots}
    def control(self):
        obj = self.sender()
        valor = obj.isChecked()
        print("Objeto ", obj.text(), ": ", valor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
