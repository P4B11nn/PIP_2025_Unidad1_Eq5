import sys
import os
import statistics
from PyQt5 import uic, QtWidgets

qtCreatorFile = "ProyectoFinal.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_cargar.clicked.connect(self.cargar)
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)

        self.calificaciones = []

    def cargar(self):
        if not os.path.exists("../Archivos/calificaciones.csv"):
            self.msj("El archivo no existe.")
            return

        try:
            with open(r"../Archivos/calificaciones.csv") as archivo:
                contenido = archivo.readlines()
                self.calificaciones = [int(x.strip()) for x in contenido if x.strip().isdigit()]
            self.actualizar_datos()
        except Exception as e:
            self.msj(f"Error al cargar: {e}")

    def agregar(self):
        try:
            texto = self.txt_calificacion.text().strip()
            if not texto.isdigit():
                self.msj("Ingrese un número válido.")
                return

            calificacion = int(texto)
            self.calificaciones.append(calificacion)
            self.actualizar_datos()
            self.txt_calificacion.clear()
        except Exception as e:
            self.msj(f"Error al agregar: {e}")

    def actualizar_datos(self):
        if not self.calificaciones:
            return

        try:
            self.txt_lista_calificaciones.setText(", ".join(map(str, self.calificaciones)))
            self.txt_promedio.setText(str(round(statistics.mean(self.calificaciones), 2)))
            self.lbl_min.setText(str(min(self.calificaciones)))
            self.lbl_max.setText(str(max(self.calificaciones)))
            self.lbl_mediana.setText(str(statistics.median(self.calificaciones)))
            self.lbl_moda.setText(str(statistics.mode(self.calificaciones)))
            self.lbl_desviacion.setText(str(round(statistics.stdev(self.calificaciones), 2)))
            self.lbl_varianza.setText(str(round(statistics.variance(self.calificaciones), 2)))
        except statistics.StatisticsError:
            self.msj("No hay suficientes datos para calcular estadísticas.")
        except Exception as e:
            self.msj(f"Error al actualizar datos: {e}")

    def guardar(self):
        try:
            with open(r"../Archivos/calificaciones.csv", "w") as archivo:
                for c in self.calificaciones:
                    archivo.write(str(c) + "\n")
            self.msj("Archivo guardado con éxito!")
        except Exception as e:
            self.msj(f"Error al guardar: {e}")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
