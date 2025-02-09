import sys
import os
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E12_Validacion_carga.ui"
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

    # Area de los Slots
    def cargar(self):
        # Verificar si el archivo existe
        if not os.path.exists("../Archivos/calificaciones.csv"):
            self.msj("El archivo no existe.")
            return
        if self.calificaciones:
            self.msj("Ya se han agregado calificaciones. No se puede cargar.")
            return

        # Verificar si el archivo está vacío
        if os.path.getsize("../Archivos/calificaciones.csv") == 0:
            self.msj("El archivo está vacío. No se puede cargar.")
            return

        try:
            with open("../Archivos/calificaciones.csv") as archivo:
                contenido = archivo.readlines()

            datos = [int(x.strip()) for x in contenido if x.strip().isdigit()]
            if not datos:
                self.msj("El archivo contiene datos no válidos.")
                return

            # Concatenar datos en lugar de sobrescribir
            self.calificaciones.extend(datos)
            self.promedio()
            self.txt_lista_calificaciones.setText(", ".join(map(str, self.calificaciones)))
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def agregar(self):
        try:
            calificacion = int(self.txt_calificaciones.text())
            self.calificaciones.append(calificacion)
            self.promedio()
        except ValueError:
            self.msj("Por favor, introduce una calificación válida.")

    def guardar(self):
        try:
            with open(r"../Archivos/calificaciones.csv", "w") as archivo:
                for c in self.calificaciones:
                    archivo.write(str(c) + "\n")
            self.msj("Archivo Guardado con Exito!")
            self.txt_calificaciones.clear()
            self.txt_lista_calificaciones.clear()
            self.txt_promedio.clear()
        except Exception as e:
            self.msj(f"Error al guardar el archivo: {e}")

    def promedio(self):
        if len(self.calificaciones) == 0:
            self.msj("No hay calificaciones para calcular el promedio.")
            return
        promedio = sum(self.calificaciones) / len(self.calificaciones)
        self.txt_promedio.setText(str(promedio))

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())