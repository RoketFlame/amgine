import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTableWidgetItem
from numpy import transpose

from all_crypto_functions import monoalphabetic_code, SomethingWrong, create_dict, add_value
from designs.mono_add_dict import Ui_Mono_Alpha_Add_Dict
from designs.mono_main import Ui_Mono_Alpha_Main
from designs.mono_use_dict import Ui_Mono_Alpha_Use_Dict
from recourse.menu_windows import InfoWindow, HistoryWindow, HelpWindow


class MonoAlphaMain(QMainWindow, Ui_Mono_Alpha_Main):
    # class MonoAlphaMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('mono_main.ui', self)  # подгрузка ui файла
        # подключение кнопок к событиям
        self.btn_add_dict.clicked.connect(self.add)
        self.btn_use_dict.clicked.connect(self.use)

    def add(self):
        self.add_dict = MonoAlphaAddDict()
        self.add_dict.show()

    def use(self):
        self.use_dict = MonoAlphaUseDict()
        self.use_dict.show()


class MonoAlphaUseDict(QMainWindow, Ui_Mono_Alpha_Use_Dict):
    # class MonoAlphaUseDict(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('mono_use_dict.ui', self)  # подгрузка ui файла
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


class MonoAlphaAddDict(QMainWindow, Ui_Mono_Alpha_Add_Dict):
    # class MonoAlphaAddDict(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('mono_add_dict.ui', self)  # подгрузка ui файла
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
