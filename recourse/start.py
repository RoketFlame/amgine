from PyQt5.QtWidgets import QMainWindow

from designs.start_window import Ui_Start_Window
from recourse.login import LoginDialog
from recourse.menu_windows import InfoWindow, HistoryWindow, HelpWindow


class StartWindow(QMainWindow, Ui_Start_Window):
    # class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.log = LoginDialog()
        # uic.loadUi('start_window.ui', self)  # Подгузка ui файла
        self.setupUi(self)
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
