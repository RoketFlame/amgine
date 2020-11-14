import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTableWidgetItem

from all_crypto_functions import encode_in_number_systems, decode_in_number_systems
from designs.number_systems_main import Ui_Number_Systems_Main
from recourse.menu_windows import InfoWindow, HistoryWindow, HelpWindow

class NumberSystemsMain(QMainWindow, Ui_Number_Systems_Main):
    # class NumberSystemsMain(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('number_systems_main.ui', self)  # подгрузка ui файла

        self.con = sqlite3.connect("record.db")
        self.cur = self.con.cursor()
        self.code_type = 'CALC_NUM'
        self.setupUi(self)
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