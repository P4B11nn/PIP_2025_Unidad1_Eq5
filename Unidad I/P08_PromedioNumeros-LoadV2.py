import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "P08_PromedioNumeros-LoadV2.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_cargar.clicked.connect(self.cargar)
        self.calificaciones = []

    #Area de los Slots
    def cargar(self):
        archivo = open(r"Archivos\calificaciones.csv")
        contenido = archivo.readlines()
        datos = [int(x) for x in contenido]
        print(datos)
        #Tarea EJ 11--En lugar de sobreescribir, concatenar
        self.calificaciones = datos
        self.promedio()
        self.txt_lista_calificaciones.setText(str(self.calificaciones))


    def agregar(self):
        calificacion = int(self.txt_calificaciones.text())
        self.calificaciones.append(calificacion)
        self.promedio()
        # Tarea EJ 12 Asegurarse de que solo se pueda cargar hasta antes de
        # Agregar la primera calificacion  -----> enables y o codigo
        self.txt_lista_calificaciones.setText(str(self.calificaciones))


    def guardar(self):
        # Tarea como comprobar que el archivo existe
        archivo = open(r"Archivos\calificaciones.csv","w")
        for c in self.calificaciones:
            archivo.write(str(c) + "\n")
        archivo.flush()
        archivo.close()
        self.msj("Archivo Guardado con Exito!")

    def promedio(self):
        prom = sum(self.calificaciones) / len(self.calificaciones)
        self.txt_promedio.setText(str(prom))

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())







