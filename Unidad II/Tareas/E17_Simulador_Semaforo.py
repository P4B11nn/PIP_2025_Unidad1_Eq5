import sys
import os
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import uic, QtWidgets


class Simulador_Semaforo(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.cargar_ui()
        self.configurar_interfaz()

    def cargar_ui(self):
        """Carga la interfaz de usuario y verifica recursos"""
        try:
            if not os.path.exists("E17_Simulador_Semaforo.ui"):
                raise FileNotFoundError("No se encuentra el archivo UI")
            uic.loadUi("E17_Simulador_Semaforo.ui", self)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error al cargar la UI: {str(e)}")
            sys.exit(1)

    def configurar_interfaz(self):
        """Configura la interfaz y los elementos del semáforo"""
        # Configurar imágenes de marca de agua
        if hasattr(self, 'label_imagen_1'):
            pixmap1 = QPixmap('../Archivos/LOGOUAT.png')
            self.label_imagen_1.setPixmap(pixmap1)
            self.label_imagen_1.setScaledContents(True)

        if hasattr(self, 'label_imagen_2'):
            pixmap2 = QPixmap('../Archivos/FIT_logo_vertical.png')
            self.label_imagen_2.setPixmap(pixmap2)
            self.label_imagen_2.setScaledContents(True)

        if hasattr(self, 'label_imagen_3'):
            pixmap3 = QPixmap('../Archivos/imgEq5.jpg')
            self.label_imagen_3.setPixmap(pixmap3)
            self.label_imagen_3.setScaledContents(True)

        # Lista de imágenes del semáforo
        self.luces = [
            '../Archivos/rojo.jpg',
            '../Archivos/verde.png',
            '../Archivos/amarillo.jpg'

        ]

        # Verificar existencia de todas las imágenes
        for imagen in self.luces + ['../Archivos/FIT_logo_vertical.png', '../Archivos/LOGOUAT.png']:
            if not os.path.exists(imagen):
                QtWidgets.QMessageBox.warning(self, "Advertencia",
                                              f"No se encuentra la imagen: {imagen}")

        # Configurar temporizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cambiar_luz)
        self.timer.start(5000)

        self.estado_actual = 0
        self.cambiar_luz()

        # Configurar botón de reinicio
        if hasattr(self, 'btn_Reiniciar'):
            self.btn_Reiniciar.clicked.connect(self.reiniciar_simulacion)
            self.btn_Reiniciar.setShortcut('R')

    def cambiar_luz(self):
        try:
            self.estado_actual = (self.estado_actual + 1) % len(self.luces)
            pixmap = QPixmap(self.luces[self.estado_actual])

            if not pixmap.isNull() and hasattr(self, 'imagen_label'):
                self.imagen_label.setPixmap(pixmap.scaled(200, 400, Qt.KeepAspectRatio))
                self.actualizar_estado_texto()
            else:
                raise Exception(f"No se pudo cargar la imagen: {self.luces[self.estado_actual]}")

        except Exception as e:
            print(f"⚠️ Error: {str(e)}")

    def actualizar_estado_texto(self):
        """Actualiza el texto del estado del semáforo"""
        estados = ["ROJO", "VERDE", "AMARILLO"]
        if hasattr(self, 'lbl_estado'):
            self.lbl_estado.setText(f"Estado: {estados[self.estado_actual]}")

    def reiniciar_simulacion(self):
        self.estado_actual = 0
        self.cambiar_luz()
        self.timer.start(5000)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Simulador_Semaforo()
    window.show()
    sys.exit(app.exec_())