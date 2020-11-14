import sqlite3
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from designs.help_window import Ui_Help_Window
from designs.history_window import Ui_History_Window
from designs.info_window import Ui_Info_Window


class InfoWindow(QMainWindow, Ui_Info_Window):
    # class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('info_window.ui', self)  # подгрузка ui файла
        self.setupUi(self)


class HelpWindow(QMainWindow, Ui_Help_Window):
    # class HelpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('help_window.ui', self)  # подгрузка ui файла
        self.setupUi(self)


class HistoryWindow(QMainWindow, Ui_History_Window):
    # class HistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('history_window.ui', self)
        self.setupUi(self)

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

