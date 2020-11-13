from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 320, 631, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.rb_lang_eng = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rb_lang_eng.setObjectName("rb_lang_eng")
        self.btn_group_lang = QtWidgets.QButtonGroup(MainWindow)
        self.btn_group_lang.setObjectName("btn_group_lang")
        self.btn_group_lang.addButton(self.rb_lang_eng)
        self.gridLayout.addWidget(self.rb_lang_eng, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.rb_lang_ru = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rb_lang_ru.setObjectName("rb_lang_ru")
        self.btn_group_lang.addButton(self.rb_lang_ru)
        self.gridLayout.addWidget(self.rb_lang_ru, 0, 1, 1, 1)
        self.rb_crypt_decode = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rb_crypt_decode.setObjectName("rb_crypt_decode")
        self.btn_group_crypt = QtWidgets.QButtonGroup(MainWindow)
        self.btn_group_crypt.setObjectName("btn_group_crypt")
        self.btn_group_crypt.addButton(self.rb_crypt_decode)
        self.gridLayout.addWidget(self.rb_crypt_decode, 1, 1, 1, 1)
        self.rb_crypt_code = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rb_crypt_code.setObjectName("rb_crypt_code")
        self.btn_group_crypt.addButton(self.rb_crypt_code)
        self.gridLayout.addWidget(self.rb_crypt_code, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 280, 131, 31))
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 101, 31))
        self.label_3.setObjectName("label_3")
        self.btn_load_text = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_text.setGeometry(QtCore.QRect(120, 250, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_load_text.sizePolicy().hasHeightForWidth())
        self.btn_load_text.setSizePolicy(sizePolicy)
        self.btn_load_text.setObjectName("btn_load_text")
        self.btn_save_text = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_text.setGeometry(QtCore.QRect(500, 250, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_text.sizePolicy().hasHeightForWidth())
        self.btn_save_text.setSizePolicy(sizePolicy)
        self.btn_save_text.setObjectName("btn_save_text")
        self.btn_code = QtWidgets.QPushButton(self.centralwidget)
        self.btn_code.setGeometry(QtCore.QRect(270, 110, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_code.sizePolicy().hasHeightForWidth())
        self.btn_code.setSizePolicy(sizePolicy)
        self.btn_code.setObjectName("btn_code")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 251, 31))
        self.label_11.setObjectName("label_11")
        self.textBrowser_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_output.setGeometry(QtCore.QRect(390, 30, 251, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_output.sizePolicy().hasHeightForWidth())
        self.textBrowser_output.setSizePolicy(sizePolicy)
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 0, 241, 31))
        self.label_2.setObjectName("label_2")
        self.textBrowser_input = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_input.setGeometry(QtCore.QRect(10, 30, 251, 211))
        self.textBrowser_input.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_input.setObjectName("textBrowser_input")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 250, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(10, 490, 631, 71))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.info = QtWidgets.QAction(MainWindow)
        self.info.setObjectName("info")
        self.help = QtWidgets.QAction(MainWindow)
        self.help.setObjectName("help")
        self.history = QtWidgets.QAction(MainWindow)
        self.history.setObjectName("history")
        self.menu.addAction(self.info)
        self.menu.addAction(self.help)
        self.menu.addAction(self.history)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Amgine Morse"))
        self.rb_lang_eng.setText(_translate("MainWindow", "ENG"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Дешифровка/шифровка</span></p></body></html>"))
        self.rb_lang_ru.setText(_translate("MainWindow", "RU"))
        self.rb_crypt_decode.setText(_translate("MainWindow", "Дешифровка"))
        self.rb_crypt_code.setText(_translate("MainWindow", "Шифровка"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Язык шифрования</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#0000ff;\">Настройки</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Загрузить текст</span></p></body></html>"))
        self.btn_load_text.setText(_translate("MainWindow", "Загрузить"))
        self.btn_save_text.setText(_translate("MainWindow", "Сохранить"))
        self.btn_code.setText(_translate("MainWindow", "→"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Ввод</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Вывод</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Сохранить текст</span></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.info.setText(_translate("MainWindow", "Инфо"))
        self.help.setText(_translate("MainWindow", "Помощь"))
        self.history.setText(_translate("MainWindow", "История"))
