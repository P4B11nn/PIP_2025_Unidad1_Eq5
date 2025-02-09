#Alex version
import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "E08_Tabla_Multiplicar.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.Slider_Numeros.setMinimum(00)
        self.Slider_Numeros.setMaximum(1000)
        self.Slider_Numeros.setSingleStep(1)
        self.Slider_Numeros.setValue(0)
        self.label_Numero.setText("0")
        self.Slider_Numeros.valueChanged.connect(self.update_table)
        self.update_table()



    #Area de los Slots
    def update_table(self):
        num = self.Slider_Numeros.value()
        self.label_Numero.setText(f"Número: {num}")

        table_text = "\n".join([f"{num} x {i} = {num * i}" for i in range(1, 11)])
        self.textEdit.setText(table_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

