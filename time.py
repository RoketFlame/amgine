import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from dialog_login import Ui_Dialog
from start_window import Ui_MainWindow_Choice
from login import Ui_MainWindow
from morse_window import Ui_Morse_MainWindow
from caesar import Ui_Caesar_Main_Window
from all_crypto_functions import *

LOGIN = ''
CIPHER = ''


class MorseMainWindow(QMainWindow, Ui_Morse_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.rb_lang_ru.setChecked(True)
        self.rb_crypt_code.setChecked(True)


class CaesarMainWindow(QMainWindow, Ui_Caesar_Main_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.code_btn.clicked.connect(self.code)
        self.load_btn.clicked.connect(self.load)
        self.save_btn.clicked.connect(self.save)
        self.rb_lang_ru.setChecked(True)
        self.rb_cap_yes.setChecked(True)
        self.rb_crypt_decode.setChecked(True)
        self.key_line_edit.setText('3')

    def code(self):
        self.shift = int(self.key_line_edit.text())
        self.ciphertext = caesar_code(self.textBrowser_1.toPlainText(), shift=self.shift)
        self.textBrowser_2.setText(self.ciphertext)

    def save(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
        f = open(fname, 'w', encoding='utf8')
        f.write(self.ciphertext)

    def load(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
        f = open(fname, 'r', encoding='utf8')
        self.text = f.read()
        self.textBrowser_1.setText(self.text)


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
            self.ciph = CaesarMainWindow()
            self.ciph.show()
        elif self.radioButton_2.isChecked():
            CIPHER = 'MORSE'
            self.morse_window = MorseMainWindow()
            self.morse_window.show()
        elif self.radioButton_3.isChecked():
            CIPHER = 'VIGENER'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec())
