# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caesar_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Caesar_Main_Window(object):
    def setupUi(self, Caesar_Main_Window):
        Caesar_Main_Window.setObjectName("Caesar_Main_Window")
        Caesar_Main_Window.resize(650, 590)
        self.centralwidget = QtWidgets.QWidget(Caesar_Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_input = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_input.setGeometry(QtCore.QRect(10, 30, 251, 211))
        self.textBrowser_input.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_input.setObjectName("textBrowser_input")
        self.btn_code = QtWidgets.QPushButton(self.centralwidget)
        self.btn_code.setGeometry(QtCore.QRect(270, 110, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_code.sizePolicy().hasHeightForWidth())
        self.btn_code.setSizePolicy(sizePolicy)
        self.btn_code.setObjectName("btn_code")
        self.textBrowser_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_output.setGeometry(QtCore.QRect(390, 30, 251, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_output.sizePolicy().hasHeightForWidth())
        self.textBrowser_output.setSizePolicy(sizePolicy)
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 251, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 0, 241, 31))
        self.label_2.setObjectName("label_2")
        self.btn_load_text = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_text.setGeometry(QtCore.QRect(120, 250, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_load_text.sizePolicy().hasHeightForWidth())
        self.btn_load_text.setSizePolicy(sizePolicy)
        self.btn_load_text.setObjectName("btn_load_text")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 250, 161, 31))
        self.label_4.setObjectName("label_4")
        self.btn_save_text = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_text.setGeometry(QtCore.QRect(500, 250, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_text.sizePolicy().hasHeightForWidth())
        self.btn_save_text.setSizePolicy(sizePolicy)
        self.btn_save_text.setObjectName("btn_save_text")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 310, 631, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.rb_lang_ru = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rb_lang_ru.setObjectName("rb_lang_ru")
        self.btn_group_lang = QtWidgets.QButtonGroup(Caesar_Main_Window)
        self.btn_group_lang.setObjectName("btn_group_lang")
        self.btn_group_lang.addButton(self.rb_lang_ru)
        self.gridLayout.addWidget(self.rb_lang_ru, 0, 1, 1, 1)
        self.rb_lang_eng = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rb_lang_eng.setObjectName("rb_lang_eng")
        self.btn_group_lang.addButton(self.rb_lang_eng)
        self.gridLayout.addWidget(self.rb_lang_eng, 0, 2, 1, 1)
        self.rb_cap_no = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rb_cap_no.setObjectName("rb_cap_no")
        self.btn_group_cap = QtWidgets.QButtonGroup(Caesar_Main_Window)
        self.btn_group_cap.setObjectName("btn_group_cap")
        self.btn_group_cap.addButton(self.rb_cap_no)
        self.gridLayout.addWidget(self.rb_cap_no, 1, 2, 1, 1)
        self.rb_crypt_code = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rb_crypt_code.setObjectName("rb_crypt_code")
        self.btn_group_crypt = QtWidgets.QButtonGroup(Caesar_Main_Window)
        self.btn_group_crypt.setObjectName("btn_group_crypt")
        self.btn_group_crypt.addButton(self.rb_crypt_code)
        self.gridLayout.addWidget(self.rb_crypt_code, 2, 2, 1, 1)
        self.rb_crypt_decode = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rb_crypt_decode.setObjectName("rb_crypt_decode")
        self.btn_group_crypt.addButton(self.rb_crypt_decode)
        self.gridLayout.addWidget(self.rb_crypt_decode, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.rb_cap_yes = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rb_cap_yes.setObjectName("rb_cap_yes")
        self.btn_group_cap.addButton(self.rb_cap_yes)
        self.gridLayout.addWidget(self.rb_cap_yes, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 280, 131, 31))
        self.label_8.setObjectName("label_8")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(10, 530, 631, 31))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.line_edit_key = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_key.setGeometry(QtCore.QRect(340, 480, 131, 31))
        self.line_edit_key.setObjectName("line_edit_key")
        self.btn_load_settings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_settings.setGeometry(QtCore.QRect(20, 480, 121, 31))
        self.btn_load_settings.setObjectName("btn_load_settings")
        self.btn_save_settings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_settings.setGeometry(QtCore.QRect(510, 480, 121, 31))
        self.btn_save_settings.setObjectName("btn_save_settings")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 480, 131, 31))
        self.label_9.setObjectName("label_9")
        Caesar_Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Caesar_Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Caesar_Main_Window.setMenuBar(self.menubar)
        self.info = QtWidgets.QAction(Caesar_Main_Window)
        self.info.setObjectName("info")
        self.help = QtWidgets.QAction(Caesar_Main_Window)
        self.help.setObjectName("help")
        self.history = QtWidgets.QAction(Caesar_Main_Window)
        self.history.setObjectName("history")
        self.menu.addAction(self.info)
        self.menu.addAction(self.help)
        self.menu.addAction(self.history)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Caesar_Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Caesar_Main_Window)

    def retranslateUi(self, Caesar_Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Caesar_Main_Window.setWindowTitle(_translate("Caesar_Main_Window", "Amgine Caesar"))
        self.btn_code.setText(_translate("Caesar_Main_Window", "→"))
        self.label.setText(_translate("Caesar_Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">Ввод</span></p></body></html>"))
        self.label_2.setText(_translate("Caesar_Main_Window", "<html><head/><body><p><span style=\" font-size:12pt;\">Вывод</span></p></body></html>"))
        self.btn_load_text.setText(_translate("Caesar_Main_Window", "Загрузить"))
        self.label_3.setText(_translate("Caesar_Main_Window", "<html><head/><body><p><span style=\" font-size:10pt;\">Загрузить текст</span></p></body></html>"))
        self.label_4.setText(_translate("Caesar_Main_Window", "<html><head/><body><p><span style=\" font-size:10pt;\">Сохранить текст</span></p></body></html>"))
        self.btn_save_text.setText(_translate("Caesar_Main_Window", "Сохранить"))
        self.label_6.setText(_translate("Caesar_Main_Window", "<html><head/><body><p><span style=\" font-size:11pt;\">Сохранение регистра</span></p></body></html>"))
        self.rb_lang_ru.setText(_translate("Caesar_Main_Window", "RU"))
        self.rb_lang_eng.setText(_translate("Caesar_Main_Window", "ENG"))
        self.rb_cap_no.setText(_translate("Caesar_Main_Window", "Нет"))
        self.rb_crypt_code.setText(_translate("Caesar_Main_Window", "Шифровка"))
        self.rb_crypt_decode.setText(_translate("Caesar_Main_Window", "Дешифровка"))
        self.label_7.setText(_translate("Caesar_Main_Window", "<html><head/><body><p><span style=\" font-size:11pt;\">Язык шифрования</span></p></body></html>"))
        self.label_5.setText(_translate("Caesar_Main_Window", "<html><head/><body><p><span style=\" font-size:11pt;\">Дешифровка/шифровка</span></p></body></html>"))
        self.rb_cap_yes.setText(_translate("Caesar_Main_Window", "Да"))
        self.label_8.setText(_translate("Caesar_Main_Window", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#0000ff;\">Настройки</span></p></body></html>"))
        self.btn_load_settings.setText(_translate("Caesar_Main_Window", "Загрузить настройки"))
        self.btn_save_settings.setText(_translate("Caesar_Main_Window", "Сохранить настройки"))
        self.label_9.setText(_translate("Caesar_Main_Window", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">Ключ шифрования</span></p></body></html>"))
        self.menu.setTitle(_translate("Caesar_Main_Window", "Меню"))
        self.info.setText(_translate("Caesar_Main_Window", "Инфо"))
        self.help.setText(_translate("Caesar_Main_Window", "Помощь"))
        self.history.setText(_translate("Caesar_Main_Window", "История"))
