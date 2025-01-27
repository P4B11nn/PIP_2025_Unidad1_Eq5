import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P02_Conversion_Metros_a_Pies.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_calcular.clicked.connect(self.metros_a_pies)



    #Area de los Slots
    def metros_a_pies(self):
        try:
            metros = float(self.txt_metros.text())
            pies = metros * 3.28084
            self.msj(f"{pies:.2f} pies")
        except ValueError:
            self.msj("Por favor, ingresa un número válido en metros.")


    def msj(self, txt):
       m = QtWidgets.QMessageBox()
       m.setText(txt)
       m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
