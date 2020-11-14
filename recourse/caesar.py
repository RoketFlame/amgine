import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTableWidgetItem

from all_crypto_functions import caesar_code, SomethingWrong
from designs.caesar_main import Ui_Caesar_Main_Window
from recourse.menu_windows import InfoWindow, HistoryWindow, HelpWindow
import recourse.just_login


class CaesarMainWindow(QMainWindow, Ui_Caesar_Main_Window):
    # class CaesarMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('caesar_main.ui', self)  # подгрузка ui файла

        self.con = sqlite3.connect("record.db")
        self.cur = self.con.cursor()
        self.code_type = 'CAESAR'
        self.setupUi(self)
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
        except ValueError:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt;'
                f' color:#ff1500;">Неверный формат настроек!</span></p></body></html>')
        except FileNotFoundError:
            pass

    def closeEvent(self, event):
        self.con.close()
