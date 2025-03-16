import sys
from PyQt5 import uic,QtWidgets
import serial as tarjeta


qtCreatorFile = "P38_ArduinoPythonGUI.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.arduino = None
        self.btn_accion.clicked.connect(self.accion)


    #Area de los Slots

    def accion(self):
        texto = self.btn_accion.text()
        com = self.txt_com.text()
        if texto == "CONECTAR":
            self.btn_accion.setText("DESCONECTAR")
        elif texto == ("DESCONECTAR"):
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
        elif texto == ("RECONECTAR"):
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("RECONECTADO")


    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
