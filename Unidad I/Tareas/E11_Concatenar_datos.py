import sys
import os
from PyQt5 import uic,QtWidgets
qtCreatorFile = "E11_Concatenar_datos.ui"
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
        # Verificar si el archivo existe
        if not os.path.exists("../Archivos/calificaciones.csv"):
            print("El archivo no existe.")
            return

        archivo = open(r"../Archivos/calificaciones.csv")
        contenido = archivo.readlines()
        archivo.close()
        print(contenido)

        datos = [int(x.strip()) for x in contenido]  # Convertir cada línea en entero, eliminando espacios
        print(datos)

        # Concatenar datos en lugar de sobrescribir
        self.calificaciones.extend(datos)
        self.promedio()
        self.txt_lista_calificaciones.setText(", ".join(map(str, self.calificaciones)))


    def agregar(self):
        calificacion = int(self.txt_calificaciones.text())
        self.calificaciones.append(calificacion)
        self.promedio()
        self.txt_lista_calificaciones.setText(", ".join(map(str, self.calificaciones)))

    def guardar(self):
        archivo = open(r"../Archivos/calificaciones.csv", "w")
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
