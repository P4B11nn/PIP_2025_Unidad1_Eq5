import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "Practica2_Eq5.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Conectar señales
        self.comboBox.currentIndexChanged.connect(self.actualizarLED)
        self.checkBox1.stateChanged.connect(self.actualizarLED)
        self.checkBox2.stateChanged.connect(self.actualizarLED)
        self.checkBox3.stateChanged.connect(self.actualizarLED)

    def actualizarLED(self):
        entrada1 = self.checkBox1.isChecked()
        entrada2 = self.checkBox2.isChecked()
        entrada3 = self.checkBox3.isChecked()
        compuerta = self.comboBox.currentText()

        if compuerta == "AND":
            resultado = entrada1 and entrada2 and entrada3
        elif compuerta == "OR":
            resultado = entrada1 or entrada2 or entrada3
        elif compuerta == "XOR":
            resultado = (entrada1 != entrada2) != entrada3
        elif compuerta == "NAND":
            resultado = not (entrada1 and entrada2 and entrada3)
        elif compuerta == "NOR":
            resultado = not (entrada1 or entrada2 or entrada3)
        elif compuerta == "XNOR":
            resultado = (entrada1 == entrada2) == entrada3
        else:
            resultado = False

        if resultado:
            self.label_led.setPixmap(QtGui.QPixmap("../Archivos/LED_ON.png"))
        else:
            self.label_led.setPixmap(QtGui.QPixmap("../Archivos/LED_OFF.png"))

        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(int(entrada1))))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(int(entrada2))))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(int(entrada3))))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(int(resultado))))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())