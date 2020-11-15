from PyQt5.QtWidgets import QDialog

import recourse.just_login
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
        # получение логина для базы данных
        if self.lineEdit.text():
            recourse.just_login.LOGIN = self.lineEdit.text()
        else:
            LOGIN = 'USER'
        self.main = ChoiceWindow()
        self.main.show()
