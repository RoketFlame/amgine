import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTableWidgetItem

from all_crypto_functions import morse_encode, morse_decode, SomethingWrong
from designs.morse_main import Ui_Morse_Main_Window
from recourse.menu_windows import InfoWindow, HistoryWindow, HelpWindow
import recourse.just_login


class MorseMainWindow(QMainWindow, Ui_Morse_Main_Window):
    # class MorseMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('morse_main.ui', self)  # подгрузка ui файла

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
        db_login = recourse.just_login.LOGIN
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
            if self.ciphertext and text:
                self.add_to_record_db(type_c)
        except SomethingWrong as s:
            self.label_error.setText(
                f'<html><head/><body><p align="center"><span style=" font-size:12pt; '
                f'color:#ff1500;">{s}</span></p></body></html>')

    def closeEvent(self, event):
        self.con.close()
