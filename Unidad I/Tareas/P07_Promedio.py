import sys
from os.path import split

from PyQt5 import uic,QtWidgets
qtCreatorFile = "P07_Promedio.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_calcular_promedio.clicked.connect(self.promedio)


    #Area de los Slots
    def promedio(self):
        try:
           numeros = self.txt_numeros.text()
           listanums =  [float(num.strip()) for num in numeros.split(',')]

           promedio = sum(listanums) / len(listanums)
           self.msj(f"Promedio de los números: {promedio:.2f}")

        except ValueError:
            self.msj("Por favor, ingresa cinco números válidos.")
    
    def msj(self, txt):
     m = QtWidgets.QMessageBox()
     m.setText(txt)
     m.exec()
            
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())