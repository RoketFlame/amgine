from PyQt5.QtWidgets import QMainWindow

from designs.choice_window import Ui_Central_MainWindow
from recourse.caesar import CaesarMainWindow
from recourse.menu_windows import InfoWindow, HistoryWindow, HelpWindow
from recourse.monoalphabet import MonoAlphaMain
from recourse.morse import MorseMainWindow
from recourse.number_systems import NumberSystemsMain
from recourse.vigenere import VigenereMainWindow


class ChoiceWindow(QMainWindow, Ui_Central_MainWindow):
    # class ChoiceWindow(QMainWindow):
    def __init__(self):
        global LOGIN
        super().__init__()
        # uic.loadUi('choice_window.ui', self)  # Подгузка ui файла
        self.setupUi(self)
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
