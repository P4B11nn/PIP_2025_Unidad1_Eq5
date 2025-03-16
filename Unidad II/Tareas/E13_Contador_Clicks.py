import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E13_Contador_Clicks.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class ContadorClicks(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.count = 0
        self.btn_click.clicked.connect(self.increment_count)
        self.btn_reset.clicked.connect(self.reset_count)

    def increment_count(self):
        self.count += 1
        self.lbl_count.setText(str(self.count))

    def reset_count(self):
        self.count = 0
        self.lbl_count.setText(str(self.count))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ContadorClicks()
    window.show()
    sys.exit(app.exec_())