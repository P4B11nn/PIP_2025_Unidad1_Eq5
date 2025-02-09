#Jesus Falzo Version
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E03_Mililitros_a_Litros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setValue(0)


        self.horizontalSlider.valueChanged.connect(self.actualizarMililitros)
        self.txt_valor.editingFinished.connect(self.actualizarSlider)


    def actualizarMililitros(self):

        mililitros = self.horizontalSlider.value()
        self.txt_valor.setText(str(mililitros))
        self.actualizarLitros(mililitros)

    def actualizarSlider(self):
        #
        try:
            mililitros = int(self.txt_valor.text())
            if 0 <= mililitros <= 1000:
                self.horizontalSlider.setValue(mililitros)
                self.actualizarLitros(mililitros)
            else:
                self.txt_valor.setText("0")
        except ValueError:
            self.txt_valor.setText("0")

    def actualizarLitros(self, mililitros):

        litros = mililitros / 1000
        self.txt_valor_2.setText(f"{litros:.3f}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

