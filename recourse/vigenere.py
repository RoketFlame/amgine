import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTableWidgetItem

from all_crypto_functions import vigenere_encode, vigenere_decode, SomethingWrong
from designs.vigenere_main import Ui_Vigenere_Main_Window
from recourse.menu_windows import InfoWindow, HistoryWindow, HelpWindow
import recourse.just_login




class VigenereMainWindow(QMainWindow, Ui_Vigenere_Main_Window):
    # class VigenereMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('vigenere_main.ui', self)  # Подгузка ui файла

        self.con = sqlite3.connect("record.db")
        self.cur = self.con.cursor()
        self.code_type = 'VIGENERE'
        self.setupUi(self)
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
        fname = QFileDialog.getOpenFileName(self, 'Выбрать текст', '', 'Текст (*.txt)')[0]
        f = open(fname, 'r', encoding='utf8')
        self.textBrowser_input.setText(f.read())
        f.close()

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
        db_login = recourse.just_login.LOGIN
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
        except ValueError:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">Неверный формат настроек!</span></p></body></html>')
        except FileNotFoundError:
            pass

    def closeEvent(self, event):
        self.con.close()
