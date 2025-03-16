import sys
from PyQt5 import uic,QtWidgets

import P1_vPython_Ejemplo as interfaz

#qtCreatorFile = "P00_Intro.ui"  #Nombre del archivo aqui
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_sumar.clicked.connect(self.sumar)


    #Area de los Slots

    def sumar(self):
        try:
            a = float(self.txt_A.text())
            b = float(self.txt_B.text())
            c = float(self.txt_C.text())
            r = a + b + c
            self.msj("La suma es:" + str(r))
        except Exception as error:
            print(error)

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
