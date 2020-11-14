import sys
import sqlite3
from numpy import transpose
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTableWidgetItem
# from start_window import Ui_Start_Window
# from login_dialog import Ui_Dialog
# from choice_window import Ui_Central_MainWindow
# from morse_main import Ui_Morse_Main_Window
# from caesar_main import Ui_Caesar_Main_Window
# from number_systems_main import Ui_Number_Systems_Main
# from help_window import Ui_Help_Window
# from info_window import Ui_Info_Window
from all_crypto_functions import *
from PyQt5 import uic

LOGIN = 'USER'


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# class StartWindow(QMainWindow, Ui_MainWindow):
class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.log = LoginDialog()
        uic.loadUi('start_window.ui', self)  # Подгузка ui файла
        # self.setupUi(self)
        # Подключения всех кнопок к событиям
        self.start_login_btn.clicked.connect(self.start)
        self.info.triggered.connect(self.show_info)
        self.help.triggered.connect(self.show_help)
        self.history.triggered.connect(self.show_history)

    def show_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()
        pass

    def show_help(self):
        self.help_window = HelpWindow()
        self.help_window.show()
        pass

    def show_history(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    def start(self):
        self.log.show()
        self.close()


# class LoginDialog(QDialog, Ui_Dialog):
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('login_dialog.ui', self)  # Подгузка ui файла
        # self.setupUi(self)
        # Подключения всех кнопок к событиям
        self.buttonBox.clicked.connect(self.run_login)

    def run_login(self):
        global LOGIN
        # получение логина для базы данных
        LOGIN = self.lineEdit.text()
        self.main = ChoiceWindow()
        self.main.show()


# class ChoiceWindow(QMainWindow, Ui_Central_MainWindow):
class ChoiceWindow(QMainWindow):
    def __init__(self):
        global LOGIN
        super().__init__()
        uic.loadUi('choice_window.ui', self)  # Подгузка ui файла
        # self.setupUi(self)
        # Подключения всех кнопок к событиям
        self.start_button.clicked.connect(self.start)
        self.info.triggered.connect(self.show_info)
        self.help.triggered.connect(self.show_help)
        self.history.triggered.connect(self.show_history)

    def show_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()
        pass

    def show_help(self):
        self.help_window = HelpWindow()
        self.help_window.show()
        pass

    def show_history(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    def start(self):
        global CIPHER
        # выбор способа шифрования
        self.crypt_t = self.type_crypt.currentText()
        if self.crypt_t == 'Шифр Цезаря':
            self.ciph = CaesarMainWindow()
            self.ciph.show()
        elif self.crypt_t == 'Азбука Морзе':
            self.morse_window = MorseMainWindow()
            self.morse_window.show()
        elif self.crypt_t == 'Шифр Вижинера':
            self.vigenere_window = VigenereMainWindow()
            self.vigenere_window.show()
        elif self.crypt_t == 'Моноалфавит':
            self.monoalph = MonoAlphaMain()
            self.monoalph.show()
        elif self.crypt_t == 'Системы счисления':
            self.number_systems = NumberSystemsMain()
            self.number_systems.show()


# class VigenereMainWindow(QMainWindow, Ui_Vigenere_Main_Window):
class VigenereMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('vigenere_main.ui', self)  # Подгузка ui файла

        self.con = sqlite3.connect("record.db")
        self.cur = self.con.cursor()
        self.code_type = 'VIGENERE'
        # self.setupUi(self)
        # выставление значений по умолчанию
        self.rb_lang_ru.setChecked(True)
        self.rb_crypt_decode.setChecked(True)
        self.btn_save_settings.setEnabled(False)
        self.line_edit_key.setText('key')
        # Подключения всех кнопок к событиям
        self.btn_code.clicked.connect(self.code)
        self.btn_load_text.clicked.connect(self.load_text)
        self.btn_save_text.clicked.connect(self.save_text)
        self.btn_save_settings.clicked.connect(self.save_settings)
        self.btn_load_settings.clicked.connect(self.load_settings)

        self.info.triggered.connect(self.show_info)
        self.help.triggered.connect(self.show_help)
        self.history.triggered.connect(self.show_history)

    def show_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()
        pass

    def show_help(self):
        self.help_window = HelpWindow()
        self.help_window.show()
        pass

    def show_history(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    # загрузка текста
    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.textBrowser_input.setText(f.read())
            f.close()
        except:
            pass

    # сохранение текста
    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(str(self.ciphertext))
            f.close()
        except:
            pass

    def add_to_record_db(self, is_d):
        global LOGIN
        db_login = LOGIN
        db_is_dec = is_d
        db_nameciph = self.code_type
        ins_value = (db_login, db_is_dec, db_nameciph)
        self.cur.execute(
            "INSERT INTO record_table(login_record, is_decode, name_cipher) VALUES(?, ?, ?)",
            (ins_value))
        self.con.commit()

    # функция кодирования
    def code(self):
        try:
            if self.rb_lang_ru.isChecked():
                self.lang = 'RU'
            else:
                self.lang = 'ENG'
            text = self.textBrowser_input.toPlainText()
            self.key = self.line_edit_key.text()
            if self.rb_crypt_code.isChecked():
                type_c = 'encode'
                self.ciphertext = vigenere_encode(self.key, text, self.lang)
            else:
                self.ciphertext = vigenere_decode(self.key, text, self.lang)
                type_c = 'decode'
            self.textBrowser_output.setText(self.ciphertext)
            if text:
                self.btn_save_settings.setEnabled(True)
            self.label_error.setText('')
            if text and self.ciphertext:
                self.add_to_record_db(type_c)
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">{s}</span></p></body></html>')

    # сохранение нстроек
    def save_settings(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.stg)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(f'{self.key} -{self.lang}')
            f.close()
        except:
            pass

    # загрузка настроек
    def load_settings(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.stg)')[0]
            f = open(fname, 'r', encoding='utf8')
            settings = f.read().split(' -')
            key, lang = settings
            self.line_edit_key.setText(key)
            if lang == 'ENG':
                self.rb_lang_eng.setChecked(True)
            else:
                self.rb_lang_ru.setChecked(True)
            f.close()
            self.label_error.setText('')
        except:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">Неверный формат настроек!</span></p></body></html>')

    def closeEvent(self, event):
        self.con.close()


# class MorseMainWindow(QMainWindow, Ui_Morse_MainWindow):
class MorseMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi('morse_main.ui', self)  # подгрузка ui файла

        self.con = sqlite3.connect("record.db")
        self.cur = self.con.cursor()
        self.code_type = 'MORSE'
        # выставление значений по умолчанию
        self.rb_lang_ru.setChecked(True)
        self.rb_crypt_decode.setChecked(True)
        # Подключения всех кнопок к событиям
        self.btn_code.clicked.connect(self.code)
        self.btn_load_text.clicked.connect(self.load_text)
        self.btn_save_text.clicked.connect(self.save_text)

        self.info.triggered.connect(self.show_info)
        self.help.triggered.connect(self.show_help)
        self.history.triggered.connect(self.show_history)

    def show_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()

    def show_help(self):
        self.help_window = HelpWindow()
        self.help_window.show()

    def show_history(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    # загрузка текста
    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.textBrowser_input.setText(f.read())
            f.close()
        except:
            pass

    # сохранение текста
    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(self.ciphertext)
            f.close()
        except:
            pass

    def add_to_record_db(self, is_d):
        global LOGIN
        db_login = LOGIN
        db_is_dec = is_d
        db_nameciph = self.code_type
        ins_value = (db_login, db_is_dec, db_nameciph)
        self.cur.execute(
            "INSERT INTO record_table(login_record, is_decode, name_cipher) VALUES(?, ?, ?)",
            (ins_value))
        self.con.commit()

    # функция кодировния
    def code(self):
        try:
            if self.rb_lang_ru.isChecked():
                self.lang = 'RU'
            else:
                self.lang = 'ENG'
            text = self.textBrowser_input.toPlainText()
            if self.rb_crypt_code.isChecked():
                self.ciphertext = morse_encode(text, self.lang)
                type_c = 'encode'
            else:
                self.ciphertext = morse_decode(text, self.lang)
                type_c = 'decode'
            self.textBrowser_output.setText(self.ciphertext)
            self.label_error.setText('')
            if self.ciphertext and text:
                self.add_to_record_db(type_c)
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt; '
                f'color:#ff1500;">{s}</span></p></body></html>')

    def closeEvent(self, event):
        self.con.close()


# class CaesarMainWindow(QMainWindow, Ui_Caesar_Main_Window):
class CaesarMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('caesar_main.ui', self)  # подгрузка ui файла

        self.con = sqlite3.connect("record.db")
        self.cur = self.con.cursor()
        self.code_type = 'CAESAR'
        # self.setupUi(self)
        # пдключение кнопок к событиям
        self.btn_code.clicked.connect(self.code)
        self.btn_load_text.clicked.connect(self.load_text)
        self.btn_save_text.clicked.connect(self.save_text)
        self.btn_save_settings.clicked.connect(self.save_settings)
        self.btn_load_settings.clicked.connect(self.load_settings)
        # выставление значение по умолчанию
        self.rb_lang_ru.setChecked(True)
        self.rb_cap_yes.setChecked(True)
        self.rb_crypt_decode.setChecked(True)
        self.line_edit_key.setText('3')
        self.btn_save_settings.setEnabled(False)

        self.info.triggered.connect(self.show_info)
        self.help.triggered.connect(self.show_help)
        self.history.triggered.connect(self.show_history)

    def show_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()
        pass

    def show_help(self):
        self.help_window = HelpWindow()
        self.help_window.show()
        pass

    def show_history(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    def add_to_record_db(self, is_d):
        global LOGIN
        db_login = LOGIN
        db_is_dec = is_d
        db_nameciph = self.code_type
        ins_value = (db_login, db_is_dec, db_nameciph)
        self.cur.execute(
            "INSERT INTO record_table(login_record, is_decode, name_cipher) VALUES(?, ?, ?)",
            (ins_value))
        self.con.commit()

    # функция кодирования
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
                type_c = 'encode'
            else:
                self.shift = -int(self.line_edit_key.text())
                type_c = 'decode'
            text = self.textBrowser_input.toPlainText()
            self.ciphertext = caesar_code(text, shift=self.shift,
                                          cap=self.cap, lang=self.lang)
            self.textBrowser_output.setText(self.ciphertext)
            if text:
                self.btn_save_settings.setEnabled(True)
            self.label_error.setText('')
            if text and self.ciphertext:
                self.add_to_record_db(type_c)
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">{s}</span></p></body></html>')
        except ValueError:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">Ключ должен быть целым числом!</span></p></body></html>')

    # сохранение текста
    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(self.ciphertext)
            f.close()
        except:
            pass

    # загрузка текста
    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.textBrowser_input.setText(f.read())
            f.close()
        except:
            pass

    # сохранение настроек
    def save_settings(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать текст', '', 'Текст (*.stg)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(f'{self.shift} -{self.cap} -{self.lang}')
            f.close()
        except:
            pass

    # загрузка настроек
    def load_settings(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.stg)')[0]
            f = open(fname, 'r', encoding='utf8')
            settings = f.read().split(' -')
            shift, cap, lang = settings
            self.line_edit_key.setText(shift)
            if bool(cap):
                self.rb_cap_yes.setChecked(True)
            else:
                self.rb_cap_no.setChecked(True)
            if lang == 'ENG':
                self.rb_lang_eng.setChecked(True)
            else:
                self.rb_lang_ru.setChecked(True)
            self.label_error.setText('')
            f.close()
        except:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">Неверный формат настроек!</span></p></body></html>')

    def closeEvent(self, event):
        self.con.close()

# class MonoAlphaMain(QMainWindow, Ui_Mono_Alpha_Main):
class MonoAlphaMain(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi('mono_main.ui', self)  # подгрузка ui файла
        # подключение кнопок к событиям
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
        uic.loadUi('mono_use_dict.ui', self)  # подгрузка ui файла
        self.con = sqlite3.connect("record.db")
        self.cur = self.con.cursor()
        self.code_type = 'MONO_ALPH'
        # подключение всех кнопок к событиям
        self.btn_code.clicked.connect(self.code)
        self.btn_save_text.clicked.connect(self.save_text)
        self.btn_load_text.clicked.connect(self.load_text)
        self.btn_load_dict.clicked.connect(self.load_dict)
        self.btn_check.clicked.connect(self.check)
        self.info.triggered.connect(self.show_info)
        self.help.triggered.connect(self.show_help)
        self.history.triggered.connect(self.show_history)
        # выставлнение значений по умолчанию
        self.success_load_dict.close()
        self.btn_code.setEnabled(False)
        self.btn_check.setEnabled(False)

    def show_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()
        pass

    def show_help(self):
        self.help_window = HelpWindow()
        self.help_window.show()
        pass

    def show_history(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    def add_to_record_db(self, is_d):
        global LOGIN
        db_login = LOGIN
        db_is_dec = is_d
        db_nameciph = self.code_type
        ins_value = (db_login, db_is_dec, db_nameciph)
        self.cur.execute(
            "INSERT INTO record_table(login_record, is_decode, name_cipher) VALUES(?, ?, ?)",
            (ins_value))
        self.con.commit()

    def check(self):
        # красивый вывод словарая
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

    # функция кодирования
    def code(self):
        try:
            self.ciphertext = monoalphabetic_code(self.textBrowser_input.toPlainText(), self.dict)
            self.textBrowser_output.setText(self.ciphertext)
            self.label_error.setText('')
            if self.ciphertext:
                self.add_to_record_db('code')
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">{s}</span></p></body></html>')

    # загрузка словаря
    def load_dict(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', 'Текст (*.dct)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.dict = eval(f.read())
            self.success_load_dict.show()
            self.btn_code.setEnabled(True)
            self.btn_check.setEnabled(True)
            self.label_error.setText('')
            f.close()
        except SyntaxError:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">Неверный формат словаря!</span></p></body></html>')
        except:
            pass

    # сохранение текста
    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(self.ciphertext)
            f.close()
        except:
            pass

    # загрузка текста
    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.textBrowser_input.setText(f.read())
            f.close()
        except:
            pass

    def closeEvent(self, event):
        self.con.close()


# class MonoAlphaAddDict(QMainWindow, Ui_Mono_Alpha_Add_Dict):
class MonoAlphaAddDict(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi('mono_add_dict.ui', self)  # подгрузка ui файла
        # подключение всех кнопок к событиям
        self.btn_add.clicked.connect(self.add)
        self.btn_check.clicked.connect(self.check)
        self.btn_save_dict.clicked.connect(self.save)
        # выставление значений по умолчанию
        self.dict = create_dict()
        self.btn_save_dict.setEnabled(False)
        self.info.triggered.connect(self.show_info)
        self.help.triggered.connect(self.show_help)
        self.history.triggered.connect(self.show_history)

    def show_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()
        pass

    def show_help(self):
        self.help_window = HelpWindow()
        self.help_window.show()
        pass

    def show_history(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    # функчия добавления в словарь
    def add(self):
        try:
            self.key = self.le_key.text()
            self.value = self.le_value.text()
            self.mirror = True if self.rb_mirrior_on.isChecked() else False
            self.automatic = True if self.rb_cap_on.isChecked() else False
            add_value(self.dict, self.key, self.value, self.automatic, self.mirror)
            self.le_key.setText('')
            self.le_value.setText('')
            self.label_error.setText('')
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">{s}</span></p></body></html>')

    # функция красивого вывода словаря
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

    # сохранение словаря
    def save(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '', 'Текст (*.dct)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(self.dict.__repr__())
            f.close()
        except:
            pass


# class NumberSystemsMain(QMainWindow, Ui_Number_Systems_Main)
class NumberSystemsMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('number_systems_main.ui', self)  # подгрузка ui файла

        self.con = sqlite3.connect("record.db")
        self.cur = self.con.cursor()
        self.code_type = 'CALC_NUM'
        # self.setupUi(self)
        # подключение всех кнопок
        self.btn_code.clicked.connect(self.code)
        self.btn_load_text.clicked.connect(self.load_text)
        self.btn_save_text.clicked.connect(self.save_text)
        # выставление значений по умолчанию
        self.rb_encode.setChecked(True)
        self.info.triggered.connect(self.show_info)
        self.help.triggered.connect(self.show_help)
        self.history.triggered.connect(self.show_history)

    def show_info(self):
        self.info_window = InfoWindow()
        self.info_window.show()
        pass

    def show_help(self):
        self.help_window = HelpWindow()
        self.help_window.show()
        pass

    def show_history(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

    # сохранение текста
    def save_text(self):
        try:
            fname = QFileDialog.getSaveFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'w', encoding='utf8')
            f.write(self.ciphertext)
            f.close()
        except:
            pass

    # загрузка текста
    def load_text(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
            f = open(fname, 'r', encoding='utf8')
            self.text = f.read()
            self.textBrowser_input.setText(self.text)
            f.close()
        except:
            pass

    def add_to_record_db(self, is_d):
        global LOGIN
        db_login = LOGIN
        db_is_dec = is_d
        db_nameciph = self.code_type
        ins_value = (db_login, db_is_dec, db_nameciph)
        self.cur.execute(
            "INSERT INTO record_table(login_record, is_decode, name_cipher) VALUES(?, ?, ?)",
            (ins_value))
        self.con.commit()

    # функция кодирования
    def code(self):
        try:
            radix = int(self.type_radix.currentText())
            text = self.textBrowser_input.toPlainText()
            if self.rb_encode.isChecked():
                self.ciphertext = encode_in_number_systems(text, radix)
                type_c = 'encode'
            else:
                self.ciphertext = decode_in_number_systems(text, radix)
                type_c = 'decode'
            self.textBrowser_output.setText(self.ciphertext)
            self.label_error.setText('')
            if self.ciphertext and text:
                self.add_to_record_db(type_c)
        except:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">Неверный формат текста!</span></p></body></html>')

    def closeEvent(self, event):
        self.con.close()


# class InfoWindow(QMainWindow, Ui_Info_Window):
class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('info_window.ui', self)  # подгрузка ui файла
        # self.setupUi(self)


# class HelpWindow(QMainWindow, Ui_Help_Window):
class HelpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('help_window.ui', self)  # подгрузка ui файла
        # self.setupUi(self)


class HistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('history_window.ui', self)

        self.con = sqlite3.connect("record.db")
        self.btn_refresh.clicked.connect(self.show_db)
        self.btn_delete.clicked.connect(self.delete)
        self.show_db()

    def show_db(self):
        res = self.con.cursor().execute("SELECT * FROM record_table").fetchall()
        self.table_bd.setColumnCount(4)
        self.table_bd.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.table_bd.setRowCount(
                self.table_bd.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table_bd.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение с базой данных
        self.con.close()

    def delete(self):
        self.con.cursor().execute('DELETE from record_table')
        self.con.commit()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
