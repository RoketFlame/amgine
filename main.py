import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from dialog_login import Ui_Dialog
from start_window import Ui_MainWindow_Choice
from login import Ui_MainWindow

LOGIN = ''
CIPHER = ''


class StartWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.log = LoginDialog()
        self.setupUi(self)
        self.start_login_btn.clicked.connect(self.start)

    def start(self):
        self.log.show()
        self.close()


class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.run_login)

    def run_login(self):
        global LOGIN
        LOGIN = self.lineEdit.text()
        self.main = ChoiceWindow()
        self.main.show()


class ChoiceWindow(QMainWindow, Ui_MainWindow_Choice):
    def __init__(self):
        global LOGIN
        super().__init__()
        self.setupUi(self)
        self.start_button.clicked.connect(self.start)
        self.radioButton.setChecked(True)

    def start(self):
        global CIPHER
        if self.radioButton.isChecked():
            CIPHER = 'CAESAR'
        elif self.radioButton_2.isChecked():
            CIPHER = 'MORSE'
        elif self.radioButton_3.isChecked():
            CIPHER = 'VIGENER'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec())
