import sys
import random
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "E12_Memorizar_Patron.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class SimonDice(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Conectar botones a funciones
        self.btn_start.clicked.connect(self.start_game)
        self.btn_red.clicked.connect(lambda: self.user_input(0))
        self.btn_green.clicked.connect(lambda: self.user_input(1))
        self.btn_blue.clicked.connect(lambda: self.user_input(2))
        self.btn_yellow.clicked.connect(lambda: self.user_input(3))

        self.pattern = []
        self.user_pattern = []
        self.current_step = 0

    def start_game(self):
        self.pattern = []
        self.user_pattern = []
        self.current_step = 0
        self.next_round()

    def next_round(self):
        self.user_pattern = []
        self.current_step = 0
        self.pattern.append(random.randint(0, 3))
        self.show_pattern()

    def show_pattern(self):
        self.disable_buttons()
        for i, color in enumerate(self.pattern):
            QtCore.QTimer.singleShot(i * 1000, lambda c=color: self.highlight_button(c))
        QtCore.QTimer.singleShot(len(self.pattern) * 1000, self.enable_buttons)

    def highlight_button(self, color):
        buttons = [self.btn_red, self.btn_green, self.btn_blue, self.btn_yellow]
        original_styles = [btn.styleSheet() for btn in buttons]
        buttons[color].setStyleSheet(original_styles[color] + "border: 2px solid white;")
        QtCore.QTimer.singleShot(500, lambda b=buttons[color], s=original_styles[color]: b.setStyleSheet(s))

    def user_input(self, color):
        self.user_pattern.append(color)
        if self.user_pattern[self.current_step] != self.pattern[self.current_step]:
            self.msj("Fallaste, intentalo de nuevo.")
            self.disable_buttons()
            return
        self.current_step += 1
        if self.current_step == len(self.pattern):
            self.next_round()

    def disable_buttons(self):
        self.btn_red.setEnabled(False)
        self.btn_green.setEnabled(False)
        self.btn_blue.setEnabled(False)
        self.btn_yellow.setEnabled(False)

    def enable_buttons(self):
        self.btn_red.setEnabled(True)
        self.btn_green.setEnabled(True)
        self.btn_blue.setEnabled(True)
        self.btn_yellow.setEnabled(True)

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SimonDice()
    window.show()
    sys.exit(app.exec_())