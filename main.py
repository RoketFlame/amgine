import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from dialog_login import Ui_Dialog
from start_window import Ui_MainWindow_Choice
from login import Ui_MainWindow
from morse_window import Ui_Morse_MainWindow
from caesar import Ui_Caesar_Main_Window
from all_crypto_functions import *
from PyQt5 import uic

LOGIN = ''
CIPHER = ''


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# class VigenereMainWindow(QMainWindow, Ui_Vigenere_Main_Window):
class VigenereMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi('vigener.ui', self)
        self.rb_lang_ru.setChecked(True)
        self.rb_crypt_decode.setChecked(True)

        self.key_line_edit.setText('key')

        self.code_btn.clicked.connect(self.code)
        self.load_btn.clicked.connect(self.load_text)
        self.save_btn.clicked.connect(self.save_text)
        self.save_settings_btn.clicked.connect(self.save_settings)
        self.save_settings_btn.setEnabled(False)

    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.textBrowser_1.setText(f.read())
        except:
            pass

    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(str(self.textBrowser_2.toPlainText()))
        except:
            pass

    def code(self):
        if self.rb_lang_ru.isChecked():
            self.lang = 'RU'
        else:
            self.lang = 'ENG'
        text = self.textBrowser_1.toPlainText()
        self.key = self.key_line_edit.text()
        if self.rb_crypt_code.isChecked():
            out_f = vigenere_encode(self.key, text, self.lang)
        else:
            out_f = vigenere_decode(self.key, text, self.lang)
        self.textBrowser_2.setText(out_f)
        self.save_settings_btn.setEnabled(True)

    def save_settings(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(f'{self.lang}')
        except:
            pass


# class MorseMainWindow(QMainWindow, Ui_Morse_MainWindow):
class MorseMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi('morse_window.ui', self)

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


# class CaesarMainWindow(QMainWindow, Ui_Caesar_Main_Window):
class CaesarMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('caesar.ui', self)
        # self.setupUi(self)

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


# class StartWindow(QMainWindow, Ui_MainWindow):
class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.log = LoginDialog()
        uic.loadUi('login.ui', self)
        # self.setupUi(self)
        self.start_login_btn.clicked.connect(self.start)

    def start(self):
        self.log.show()
        self.close()


# class LoginDialog(QDialog, Ui_Dialog):
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('dialog_login.ui', self)
        # self.setupUi(self)
        self.buttonBox.clicked.connect(self.run_login)

    def run_login(self):
        global LOGIN
        LOGIN = self.lineEdit.text()
        self.main = ChoiceWindow()
        self.main.show()


# class ChoiceWindow(QMainWindow, Ui_MainWindow_Choice):
class ChoiceWindow(QMainWindow):
    def __init__(self):
        global LOGIN
        super().__init__()
        uic.loadUi('start_window.ui', self)
        # self.setupUi(self)
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
            self.vigenere_window = VigenereMainWindow()
            self.vigenere_window.show()
        elif self.radioButton_4:
            self.monoalph = MonoAlphaMain()
            self.monoalph.show()


# class MonoAlphaMain(QMainWindow, Ui_Mono_Alpha_Main):
class MonoAlphaMain(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi('mono_main.ui', self)
        self.btn_add_dict.clicked.connect(self.add)
        self.btn_use_dict.clicked.connect(self.use)

    def add(self):
        self.add_dict = MonoAlphaAddDict()
        self.add_dict.show()

    def use(self):
        self.use_dict = MonoAlphaUseDict()
        self.use_dict.show()


# class MonoAlphaUseDict(QMainWindow, Ui_Mono_Alpha_Use_Dict):
class MonoAlphaUseDict(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi('mono_use_dict.ui', self)
        self.btn_code.clicked.connect(self.code)
        self.btn_load.clicked.connect(self.load_dict)
        self.btn_save.clicked.connect(self.save)
        self.success_load_dict.close()

    def code(self):
        self.ciphertext = monoalphabetic_code(self.input_tB.toPlainText(), self.dict)
        self.out_tB.setText(self.ciphertext)

    def load_dict(self):
        try:
            fname = QFileDialog.getLoadFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.dict = f.read()
            self.success_load_dict.show()
        except:
            pass

    def save(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(self.ciphertext)
        except:
            pass


# class MonoAlphaAddDict(QMainWindow, Ui_Mono_Alpha_Add_Dict):
class MonoAlphaAddDict(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi('mono_add_dict.ui', self)
        self.btn_add.clicked.connect(self.add)
        self.btn_check.clicked.connect(self.check)
        self.btn_save_dict.clicked.connect(self.save)
        self.dict = create_dict()

    def add(self):
        self.key = self.le_key.text()
        self.value = self.le_value.text()
        self.mirrior = True if self.rb_mirrior_on.isChecked() else False
        self.automatic = True if self.rb_cap_on.isChecked() else False
        add_value(self.dict, self.key, self.value, self.automatic, self.mirrior)

    def check(self):
        self.textb_check.setText(self.dict.__str__())
        pass

    def save(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
