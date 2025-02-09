#Jesus Falzo Version
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E02_Hrs_a_Seg.ui"  # Nombre del archivo .ui que creaste en Qt Designer
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Configurar Sliders
        self.horizontalSlider.setMinimum(0)    # Horas (0-23)
        self.horizontalSlider.setMaximum(23)
        self.horizontalSlider.valueChanged.connect(self.actualizarHora)

        self.horizontalSlider_2.setMinimum(0)  # Minutos (0-59)
        self.horizontalSlider_2.setMaximum(59)
        self.horizontalSlider_2.valueChanged.connect(self.actualizarMinuto)

        self.horizontalSlider_3.setMinimum(0)  # Segundos (0-59)
        self.horizontalSlider_3.setMaximum(59)
        self.horizontalSlider_3.valueChanged.connect(self.actualizarSegundo)

        # Inicializar valores
        self.actualizarHora()
        self.actualizarMinuto()
        self.actualizarSegundo()

    def actualizarHora(self):
        hora = self.horizontalSlider.value()
        self.txt_valor.setText(str(hora))
        self.actualizarSegundosTotales()

    def actualizarMinuto(self):
        minuto = self.horizontalSlider_2.value()
        self.txt_valor_3.setText(str(minuto))
        self.actualizarSegundosTotales()

    def actualizarSegundo(self):
        segundo = self.horizontalSlider_3.value()
        self.txt_valor_4.setText(str(segundo))
        self.actualizarSegundosTotales()

    def actualizarSegundosTotales(self):
        hora = self.horizontalSlider.value()
        minuto = self.horizontalSlider_2.value()
        segundo = self.horizontalSlider_3.value()
        segundos_totales = hora * 3600 + minuto * 60 + segundo
        self.txt_valor_2.setText(str(segundos_totales))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


