import sys
from numpy import transpose
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
# from dialog_login import Ui_Dialog
# from start_window import Ui_MainWindow_Choice
# from login import Ui_MainWindow
# from morse_window import Ui_Morse_MainWindow
# from caesar import Ui_Caesar_Main_Window
# from choice_window import Ui_Central_MainWindow
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
        uic.loadUi('vigenere_main.ui', self)
        self.rb_lang_ru.setChecked(True)
        self.rb_crypt_decode.setChecked(True)

        self.line_edit_key.setText('key')

        self.btn_code.clicked.connect(self.code)
        self.btn_load_text.clicked.connect(self.load_text)
        self.btn_save_text.clicked.connect(self.save_text)
        self.save_settings_btn.clicked.connect(self.save_settings)
        self.save_settings_btn.setEnabled(False)

    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.textBrowser_input.setText(f.read())
            f.close()
        except:
            pass

    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(str(self.textBrowser_output.toPlainText()))
            f.close()
        except:
            pass

    def code(self):
        try:
            if self.rb_lang_ru.isChecked():
                self.lang = 'RU'
            else:
                self.lang = 'ENG'
            text = self.textBrowser_input.toPlainText()
            self.key = self.line_edit_key.text()
            if self.rb_crypt_code.isChecked():
                self.res = vigenere_encode(self.key, text, self.lang)
            else:
                self.res = vigenere_decode(self.key, text, self.lang)
            self.textBrowser_output.setText(self.res)
            if text:
                self.save_settings_btn.setEnabled(True)
            self.label_error.setText('')
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">{s}</span></p></body></html>')

    def save_settings(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(f'{self.key} -{self.lang}')
            f.close()
        except:
            pass


# class MorseMainWindow(QMainWindow, Ui_Morse_MainWindow):
class MorseMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi('morse_main.ui', self)

        self.rb_lang_ru.setChecked(True)
        self.rb_crypt_decode.setChecked(True)

        self.btn_code.clicked.connect(self.code)
        self.btn_load_text.clicked.connect(self.load_text)
        self.btn_save_text.clicked.connect(self.save_text)
        self.btn_save_settings.clicked.connect(self.save_settings)
        self.btn_save_settings.setEnabled(False)

    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.textBrowser_input.setText(f.read())
            f.close()
        except:
            pass

    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(str(self.textbrowser_output.toPlainText()))
            f.close()
        except:
            pass

    def code(self):
        try:
            if self.rb_lang_ru.isChecked():
                self.lang = 'RU'
            else:
                self.lang = 'ENG'
            text = self.textBrowser_input.toPlainText()
            if self.rb_crypt_code.isChecked():
                out_f = morse_encode(text, self.lang)
            else:
                out_f = morse_decode(text, self.lang)
            self.textBrowser_output.setText(out_f)
            if text:
                self.btn_save_settings.setEnabled(True)
            self.label_error.setText('')
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt; '
                f'color:#ff1500;">{s}</span></p></body></html>')

    def save_settings(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(f'{self.lang}')
            f.close()
        except:
            pass


# class CaesarMainWindow(QMainWindow, Ui_Caesar_Main_Window):
class CaesarMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('caesar_main.ui', self)
        # self.setupUi(self)

        self.btn_code.clicked.connect(self.code)
        self.btn_load_text.clicked.connect(self.load_text)
        self.btn_save_text.clicked.connect(self.save_text)
        self.btn_save_settings.clicked.connect(self.save_settings)
        self.rb_lang_ru.setChecked(True)
        self.rb_cap_yes.setChecked(True)
        self.rb_crypt_decode.setChecked(True)
        self.line_edit_key.setText('3')
        self.btn_save_settings.setEnabled(False)

    def code(self):
        try:
            if self.rb_lang_ru.isChecked():
                self.lang = 'RU'
            elif self.rb_lang_eng.isChecked():
                self.lang = 'ENG'

            if self.rb_cap_yes.isChecked():
                self.cap = True
            else:
                self.cap = False

            if self.rb_crypt_code.isChecked():
                self.shift = int(self.line_edit_key.text())
            else:
                self.shift = -int(self.line_edit_key.text())
            text = self.textBrowser_input.toPlainText()
            self.ciphertext = caesar_code(text, shift=self.shift,
                                          cap=self.cap, lang=self.lang)
            self.textBrowser_output.setText(self.ciphertext)
            if text:
                self.btn_save_settings.setEnabled(True)
            self.label_error.setText('')
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">{s}</span></p></body></html>')
        except ValueError:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">Ключ должен быть целым числом</span></p></body></html>')

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
            self.textBrowser_input.setText(self.text)
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
        uic.loadUi('start_window.ui', self)
        # self.setupUi(self)
        self.start_login_btn.clicked.connect(self.start)

    def start(self):
        self.log.show()
        self.close()


# class LoginDialog(QDialog, Ui_Dialog):
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('login_dialog.ui', self)
        # self.setupUi(self)
        self.buttonBox.clicked.connect(self.run_login)

    def run_login(self):
        global LOGIN
        LOGIN = self.lineEdit.text()
        self.main = ChoiceWindow()
        self.main.show()


# class ChoiceWindow(QMainWindow, Ui_Central_MainWindow):
class ChoiceWindow(QMainWindow):
    def __init__(self):
        global LOGIN
        super().__init__()
        uic.loadUi('choice_window.ui', self)
        # self.setupUi(self)
        self.start_button.clicked.connect(self.start)

    def start(self):
        global CIPHER
        self.crypt_t = self.type_crypt.currentText()
        if self.crypt_t == 'Шифр Цезаря':
            CIPHER = 'CAESAR'
            self.ciph = CaesarMainWindow()
            self.ciph.show()
        elif self.crypt_t == 'Азбука Морзе':
            CIPHER = 'MORSE'
            self.morse_window = MorseMainWindow()
            self.morse_window.show()
        elif self.crypt_t == 'Шифр Вижинера':
            CIPHER = 'VIGENER'
            self.vigenere_window = VigenereMainWindow()
            self.vigenere_window.show()
        elif self.crypt_t == 'Моноалфавит':
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
        self.btn_save_text.clicked.connect(self.save_text)
        self.btn_load_text.clicked.connect(self.load_text)
        self.btn_load_dict.clicked.connect(self.load_dict)
        self.btn_check.clicked.connect(self.check)
        self.success_load_dict.close()
        self.btn_code.setEnabled(False)
        self.btn_check.setEnabled(False)

    def check(self):
        out = []
        res = []
        for i, key_val in enumerate(list(self.dict.items())[2:]):
            key, val = key_val
            res.append(f'{key} : {val}')
            if i % 7 == 6:
                out.append(res)
                res = []
        for i in range(7 - len(res)):
            res.append('')
        out.append(res)
        out = transpose(out)
        ready_out = ''
        for line in out:
            ready_out += ' | '.join(line) + '\n'
        self.textBrowser_check.setText(ready_out)

    def code(self):
        try:
            self.ciphertext = monoalphabetic_code(self.textBrowser_input.toPlainText(), self.dict)
            self.textBrowser_output.setText(self.ciphertext)
            self.label_error.setText('')
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">{s}</span></p></body></html>')

    def load_dict(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', 'Текст (*.dct)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.dict = eval(f.read())
            self.success_load_dict.show()
            self.btn_code.setEnabled(True)
            self.btn_check.setEnabled(True)
            self.label_error.setText('')
        except SyntaxError:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">Неверный формат словаря!</span></p></body></html>')
        except:
            pass

    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(self.ciphertext)
        except:
            pass

    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.textBrowser_input.setText(f.read())
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
        self.btn_save_dict.setEnabled(False)

    def add(self):
        try:
            self.key = self.le_key.text()
            self.value = self.le_value.text()
            self.mirrior = True if self.rb_mirrior_on.isChecked() else False
            self.automatic = True if self.rb_cap_on.isChecked() else False
            add_value(self.dict, self.key, self.value, self.automatic, self.mirrior)
            self.le_key.setText('')
            self.le_value.setText('')
            self.label_error.setText('')
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">{s}</span></p></body></html>')

    def check(self):
        out = []
        res = []
        for i, key_val in enumerate(list(self.dict.items())[2:]):
            key, val = key_val
            res.append(f'{key} : {val}')
            if i % 7 == 6:
                out.append(res)
                res = []
        if res:
            for i in range(7 - len(res)):
                res.append('')
            out.append(res)
        out = transpose(out)
        ready_out = ''
        for line in out:
            ready_out += ' | '.join(line) + '\n'
        self.textBrowser_check.setText(ready_out)
        if len(self.dict) > 2:
            self.btn_save_dict.setEnabled(True)

    def save(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.dct)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(self.dict.__repr__())
            f.close()
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
