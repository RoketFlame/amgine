from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_History_Window(object):
    def setupUi(self, History_window):
        History_window.setObjectName("History_window")
        History_window.resize(531, 488)
        self.centralwidget = QtWidgets.QWidget(History_window)
        self.centralwidget.setObjectName("centralwidget")
        self.table_bd = QtWidgets.QTableWidget(self.centralwidget)
        self.table_bd.setGeometry(QtCore.QRect(10, 170, 511, 271))
        self.table_bd.setObjectName("table_bd")
        self.table_bd.setColumnCount(0)
        self.table_bd.setRowCount(0)
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(150, 120, 231, 23))
        self.btn_refresh.setObjectName("btn_refresh")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 509, 78))
        self.label.setObjectName("label")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(404, 450, 121, 31))
        self.btn_delete.setObjectName("btn_delete")
        History_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(History_window)
        QtCore.QMetaObject.connectSlotsByName(History_window)

    def retranslateUi(self, History_window):
        _translate = QtCore.QCoreApplication.translate
        History_window.setWindowTitle(_translate("History_window", "История"))
        self.btn_refresh.setText(_translate("History_window", "Обновить табл"))
        self.label.setText(_translate("History_window",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Отображение истории кодировок</span></p></body></html>"))
        self.btn_delete.setText(_translate("History_window", "Очистить историю"))
