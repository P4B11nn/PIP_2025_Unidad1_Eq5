import sys
from PyQt5 import QtCore, QtWidgets, uic

qtCreatorFile = "E15_JuegoGato.ui"  # Nombre del archivo UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Inicializar el turno
        self.turn = 'X'

        # Conectar botones
        self.buttons = [
            self.button_1, self.button_2, self.button_3,
            self.button_4, self.button_5, self.button_6,
            self.button_7, self.button_8, self.button_9
        ]
        for button in self.buttons:
            button.clicked.connect(self.make_move)
        self.button_reset.clicked.connect(self.reset_game)

        # Mostrar la ventana
        self.show()

    def make_move(self):
        button = self.sender()
        if button.text() == '':
            button.setText(self.turn)
            if self.check_winner():
                self.label_status.setText(f'Ganador: {self.turn}')
                self.disable_buttons()
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'
                self.label_status.setText(f'Turno de {self.turn}')

    def check_winner(self):
        winning_combinations = [
            [self.button_1, self.button_2, self.button_3],
            [self.button_4, self.button_5, self.button_6],
            [self.button_7, self.button_8, self.button_9],
            [self.button_1, self.button_4, self.button_7],
            [self.button_2, self.button_5, self.button_8],
            [self.button_3, self.button_6, self.button_9],
            [self.button_1, self.button_5, self.button_9],
            [self.button_3, self.button_5, self.button_7]
        ]
        for combination in winning_combinations:
            if combination[0].text() == combination[1].text() == combination[2].text() != '':
                return True
        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.setEnabled(False)

    def reset_game(self):
        self.turn = 'X'
        self.label_status.setText(f'Turno de {self.turn}')
        for button in self.buttons:
            button.setText('')
            button.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())