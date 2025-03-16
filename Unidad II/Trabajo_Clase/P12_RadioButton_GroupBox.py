import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P11_RadioButton_GroupBox.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.rb_gato.clicked.connect(self.gato)
        self.rb_perro.clicked.connect(self.perro)
        self.rb_hamster.clicked.connect(self.hamster)
        self.rb_negro.toggle.connect(self.negro)
        self.rb_rojo.toggle.connect(self.rojo)
        self.rb_azul.toggle.connect(self.azul)




    #Area de los Slots

    def gato(self):
        v = self.rb_negro.isChecked()
        print("Gato")

    def perro(self):
        v = self.rb_negro.isChecked()
        print("Perro")

    def hamster(self):
        v = self.rb_negro.isChecked()
        print("Hamster")

    def negro(self):
        v = self.rb_negro.isChecked()
        print("negro")

    def rojo(self):
        v = self.rb_negro.isChecked()
        print("rojo")

    def azul(self):
        v = self.rb_negro.isChecked()
        print("azul")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
