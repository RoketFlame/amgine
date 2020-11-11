import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from dialog_login import Ui_Dialog
from start_window import Ui_MainWindow_Choice
from login import Ui_MainWindow
from morse_window import Ui_Morse_MainWindow
from caesar import Ui_Caesar_Main_Window
from all_crypto_functions import *

LOGIN = ''
CIPHER = ''


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MorseMainWindow(QMainWindow, Ui_Morse_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rb_lang_ru.setChecked(True)
        self.rb_crypt_decode.setChecked(True)

        self.code_btn.clicked.connect(self.code)
        self.load_btn.clicked.connect(self.load_text)
        self.save_btn.clicked.connect(self.save_text)
        self.save_settings_btn.clicked.connect(self.save_settings)
        self.save_settings_btn.setEnabled(False)

    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.textwid_1.setText(f.read())
        except:
            pass

    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(str(self.textwid_2.toPlainText()))
        except:
            pass

    def code(self):
        if self.rb_lang_ru.isChecked():
            self.lang = 'RU'
        else:
            self.lang = 'ENG'
        text = self.textwid_1.toPlainText()
        if self.rb_crypt_code.isChecked():
            out_f = morse_encode(text, self.lang)
        else:
            out_f = morse_decode(text, self.lang)
        self.textwid_2.setText(out_f)
        self.save_settings_btn.setEnabled(True)

    def save_settings(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(f'{self.lang}')
        except:
            pass


class CaesarMainWindow(QMainWindow, Ui_Caesar_Main_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.code_btn.clicked.connect(self.code)
        self.load_btn.clicked.connect(self.load_text)
        self.save_btn.clicked.connect(self.save_text)
        self.save_key_btn.clicked.connect(self.save_settings)
        self.rb_lang_ru.setChecked(True)
        self.rb_cap_yes.setChecked(True)
        self.rb_crypt_decode.setChecked(True)
        self.key_line_edit.setText('3')
        self.save_key_btn.setEnabled(False)

    def code(self):
        if self.rb_lang_ru.isChecked():
            self.lang = 'RU'
        elif self.rb_lang_eng.isChecked():
            self.lang = 'ENG'

        if self.rb_cap_yes.isChecked():
            self.cap = True
        else:
            self.cap = False

        if self.rb_crypt_code.isChecked():
            self.shift = int(self.key_line_edit.text())
        else:
            self.shift = -int(self.key_line_edit.text())

        self.ciphertext = caesar_code(self.textBrowser_1.toPlainText(), shift=self.shift,
                                      cap=self.cap, lang=self.lang)
        self.textBrowser_2.setText(self.ciphertext)
        self.save_key_btn.setEnabled(True)

    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(self.ciphertext)
            f.close()
        except:
            pass

    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.text = f.read()
            self.textBrowser_1.setText(self.text)
            f.close()
        except:
            pass

    def save_settings(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(f'{self.shift} -{self.cap} -{self.lang}')
            f.close()
        except:
            pass


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
    sys.excepthook = except_hook
    sys.exit(app.exec())
