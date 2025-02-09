#Mi version
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E04_Metros_a_Km.ui"  # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.slider_metros.setMinimum(00)
        self.slider_metros.setMaximum(10000)
        self.slider_metros.setSingleStep(10)
        self.slider_metros.setValue(0)
        self.slider_metros.valueChanged.connect(self.actualizar_valores)
        self.txt_metros.setText("0")
        self.txt_kilometros.setText("0.0")
        self.slider_metros.valueChanged.connect(self.actualizar_valores)

    # Area de los Slots
    def actualizar_valores(self):
        metros = self.slider_metros.value()
        kilometros = metros / 1000
        self.txt_metros.setText(f"{metros} metros")
        self.txt_kilometros.setText(f"{kilometros:.2f} kilómetros")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
