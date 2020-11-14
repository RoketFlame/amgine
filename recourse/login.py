from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTableWidgetItem

from designs.login_dialog import Ui_Dialog
from recourse.choice import ChoiceWindow


class LoginDialog(QDialog, Ui_Dialog):
    # class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        # uic.loadUi('login_dialog.ui', self)  # Подгузка ui файла
        self.setupUi(self)
        # Подключения всех кнопок к событиям
        self.buttonBox.clicked.connect(self.run_login)

    def run_login(self):
        global LOGIN
        # получение логина для базы данных
        LOGIN = self.lineEdit.text()
        self.main = ChoiceWindow()
        self.main.show()
