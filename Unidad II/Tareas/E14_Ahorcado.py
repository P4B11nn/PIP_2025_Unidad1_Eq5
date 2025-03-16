import sys
import random
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "E14_Ahorcado.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Conectar botones a funciones
        self.btn_adivinar.clicked.connect(self.adivinar_letra)
        self.btn_reset.clicked.connect(self.reset)
        self.image_head.setVisible(False)
        self.image_arm_left.setVisible(False)
        self.image_arm_right.setVisible(False)
        self.image_body.setVisible(False)
        self.image_leg_left.setVisible(False)
        self.image_leg_right.setVisible(False)
        self.label_1.setReadOnly(True)
        self.label_2.setReadOnly(True)
        self.label_3.setReadOnly(True)
        self.label_4.setReadOnly(True)
        self.label_5.setReadOnly(True)
        self.palabras = [ "amigo", "barco", "cielo", "dardo", "esmal", "fuego", "ganso", "huevo", "islas", "joven",
        "karma", "lente", "mango", "nieve", "oasis", "piano", "queso", "ratón", "silla", "tigre", "verde"]
        self.palabra = random.choice(self.palabras)
        self.labels = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5]
        self.init_labels()
        self.errores = 0

    def init_labels(self, letra=None):
        for label in self.labels:
            label.setText(" ")

    def mostrar_parte_cuerpo(self):
        partes_cuerpo = [
            self.image_head,
            self.image_arm_left,
            self.image_arm_right,
            self.image_body,
            self.image_leg_left,
            self.image_leg_right
        ]
        if self.errores < len(partes_cuerpo):
            partes_cuerpo[self.errores].setVisible(True)
        if self.errores == 5:
            self.msj("Has perdido")
            self.reset()

    def hide_label(self):
        #Ocultar label con su propiedad setVisible
        self.label_image.setVisible(False)

    def show_label(self):
        #Mostrar el label con true
        self.label_image.setVisible(True)

    def adivinar_letra(self):
        letra = self.txt_letra.text()
        if letra in self.palabra:
            for i, l in enumerate(self.palabra):
                if l == letra:
                    self.labels[i].setText(letra)
            if "".join([label.text() for label in self.labels]) == self.palabra:
                self.msj("Has ganado")
                self.reset()
        else:
            self.msj("La letra no está en la palabra")
            self.mostrar_parte_cuerpo()
            self.errores += 1

    def reset(self):
        self.palabra = random.choice(self.palabras)
        self.init_labels()
        self.errores = 0
        self.image_head.setVisible(False)
        self.image_arm_left.setVisible(False)
        self.image_arm_right.setVisible(False)
        self.image_body.setVisible(False)
        self.image_leg_left.setVisible(False)
        self.image_leg_right.setVisible(False)
        self.txt_letra.setText("")


    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())