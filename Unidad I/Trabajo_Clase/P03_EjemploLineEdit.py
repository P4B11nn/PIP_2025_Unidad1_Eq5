import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P03_EjemploLineEdit.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_saludar.clicked.connect(self.saludar)



    #Area de los Slots
    def saludar(self):
            nombre = self.txt_nombre.text()
            # print("hola")
            self.msj("Hola! " + nombre+ " buen dia! :D ")

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())