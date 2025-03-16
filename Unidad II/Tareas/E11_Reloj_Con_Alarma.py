import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtCreatorFile = "E11_Reloj_Con_Alarma.ui"  # Nombre del archivo UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar botones
        self.btn_alarma.clicked.connect(self.fijar_alarma)
        self.btn_detener.clicked.connect(self.detener_alarma)

        # Inicializar reloj
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.actualizar_reloj)
        self.timer.start(1000)

        # Inicializar alarma
        self.alarma_hora = None
        self.alarma_activa = False

        # Mostrar la hora actual
        self.actualizar_reloj()

    def actualizar_reloj(self):
        """Actualiza la hora actual en la interfaz."""
        hora_actual = QtCore.QTime.currentTime().toString("hh:mm:ss")
        self.lbl_reloj.setText(hora_actual)
        if self.alarma_activa and self.alarma_hora == QtCore.QTime.currentTime().toString("hh:mm"):
            self.sonar_alarma()

    def fijar_alarma(self):
        """Fija la alarma a la hora seleccionada."""
        self.alarma_hora = self.time_alarma.time().toString("hh:mm")
        self.alarma_activa = True
        self.lbl_estado.setText("Alarma fijada para las " + self.alarma_hora)
        print(f"Alarma fijada para las {self.alarma_hora}")

    def detener_alarma(self):
        """Detiene la alarma."""
        self.alarma_activa = False
        self.lbl_estado.setText("Alarma detenida")
        print("Alarma detenida")

    def sonar_alarma(self):
        """Acciones a realizar cuando suena la alarma."""
        self.alarma_activa = False
        self.lbl_estado.setText("¡Alarma sonando!")
        QtWidgets.QMessageBox.information(self, "Alarma", "¡Es hora!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())