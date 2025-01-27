import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P06_PromedioNumeros.ui"  #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.calificaciones = []

    #Area de los Slots
    def agregar(self):
        calificacion = int(self.txt_calificacion.text())
        self.calificaciones.append(calificacion)
        prom = sum(self.calificaciones) / len(self.calificaciones)
        self.txt_promedio.setText(str(prom))


    def guardar(self):
        # Tarea COMO COMPRUEBO QUE EL ARCHIVO EXISTE
        archivo = open(r"Archivos\calificaciones.csv","w")
        for c in self.calificaciones:
            archivo.write(str(c) + "\n")
        archivo.flush()
        archivo.close()
        self.msj("Archivo Guardado con Exito!")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
