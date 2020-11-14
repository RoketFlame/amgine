# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mono_use_dict.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mono_Alpha_Use_Dict(object):
    def setupUi(self, Mono_Alpha_Use_Dict):
        Mono_Alpha_Use_Dict.setObjectName("Mono_Alpha_Use_Dict")
        Mono_Alpha_Use_Dict.setEnabled(True)
        Mono_Alpha_Use_Dict.resize(650, 570)
        self.centralwidget = QtWidgets.QWidget(Mono_Alpha_Use_Dict)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_code = QtWidgets.QPushButton(self.centralwidget)
        self.btn_code.setGeometry(QtCore.QRect(270, 110, 111, 41))
        self.btn_code.setObjectName("btn_code")
        self.textBrowser_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_output.setGeometry(QtCore.QRect(390, 30, 256, 211))
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 251, 31))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 0, 241, 31))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 111, 31))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.btn_load_dict = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_dict.setGeometry(QtCore.QRect(140, 320, 101, 31))
        self.btn_load_dict.setObjectName("btn_load_dict")
        self.success_load_dict = QtWidgets.QLabel(self.centralwidget)
        self.success_load_dict.setEnabled(True)
        self.success_load_dict.setGeometry(QtCore.QRect(270, 320, 221, 31))
        self.success_load_dict.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.success_load_dict.setObjectName("success_load_dict")
        self.textBrowser_input = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_input.setGeometry(QtCore.QRect(10, 30, 251, 211))
        self.textBrowser_input.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_input.setObjectName("textBrowser_input")
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 250, 101, 31))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 101, 31))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(10, 510, 631, 31))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.textBrowser_check = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_check.setGeometry(QtCore.QRect(250, 360, 391, 141))
        self.textBrowser_check.setObjectName("textBrowser_check")
        self.btn_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check.setGeometry(QtCore.QRect(140, 360, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_check.sizePolicy().hasHeightForWidth())
        self.btn_check.setSizePolicy(sizePolicy)
        self.btn_check.setObjectName("btn_check")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 360, 121, 31))
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(-4, -8, 660, 561))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("background.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.btn_code.raise_()
        self.textBrowser_output.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.btn_load_dict.raise_()
        self.success_load_dict.raise_()
        self.textBrowser_input.raise_()
        self.btn_load_text.raise_()
        self.btn_save_text.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_error.raise_()
        self.textBrowser_check.raise_()
        self.btn_check.raise_()
        self.label_6.raise_()
        Mono_Alpha_Use_Dict.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mono_Alpha_Use_Dict)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Mono_Alpha_Use_Dict.setMenuBar(self.menubar)
        self.info = QtWidgets.QAction(Mono_Alpha_Use_Dict)
        self.info.setObjectName("info")
        self.help = QtWidgets.QAction(Mono_Alpha_Use_Dict)
        self.help.setObjectName("help")
        self.history = QtWidgets.QAction(Mono_Alpha_Use_Dict)
        self.history.setObjectName("history")
        self.menu.addAction(self.info)
        self.menu.addAction(self.help)
        self.menu.addAction(self.history)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Mono_Alpha_Use_Dict)
        QtCore.QMetaObject.connectSlotsByName(Mono_Alpha_Use_Dict)

    def retranslateUi(self, Mono_Alpha_Use_Dict):
        _translate = QtCore.QCoreApplication.translate
        Mono_Alpha_Use_Dict.setWindowTitle(_translate("Mono_Alpha_Use_Dict", "Amgine Monoalphabet"))
        self.btn_code.setText(_translate("Mono_Alpha_Use_Dict", "→"))
        self.label.setText(_translate("Mono_Alpha_Use_Dict", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Ввод</span></p></body></html>"))
        self.label_2.setText(_translate("Mono_Alpha_Use_Dict", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Вывод</span></p></body></html>"))
        self.label_5.setText(_translate("Mono_Alpha_Use_Dict", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Загрузить словарь</span></p></body></html>"))
        self.btn_load_dict.setText(_translate("Mono_Alpha_Use_Dict", "Загрузить"))
        self.success_load_dict.setText(_translate("Mono_Alpha_Use_Dict", "<html><head/><body><p><span style=\" font-size:10pt; color:#169100;\">Словарь загружен успешно!</span></p></body></html>"))
        self.btn_load_text.setText(_translate("Mono_Alpha_Use_Dict", "Загрузить"))
        self.btn_save_text.setText(_translate("Mono_Alpha_Use_Dict", "Сохранить"))
        self.label_4.setText(_translate("Mono_Alpha_Use_Dict", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Сохранить текст</span></p></body></html>"))
        self.label_3.setText(_translate("Mono_Alpha_Use_Dict", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Загрузить текст</span></p></body></html>"))
        self.textBrowser_check.setHtml(_translate("Mono_Alpha_Use_Dict", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.btn_check.setText(_translate("Mono_Alpha_Use_Dict", "Проверить"))
        self.label_6.setText(_translate("Mono_Alpha_Use_Dict", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Проверить словарь</span></p></body></html>"))
        self.menu.setTitle(_translate("Mono_Alpha_Use_Dict", "Меню"))
        self.info.setText(_translate("Mono_Alpha_Use_Dict", "Инфо"))
        self.help.setText(_translate("Mono_Alpha_Use_Dict", "Помощь"))
        self.history.setText(_translate("Mono_Alpha_Use_Dict", "История"))
