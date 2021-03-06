from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Number_Systems_Main(object):
    def setupUi(self, Number_Systems_Main):
        Number_Systems_Main.setObjectName("Number_Systems_Main")
        Number_Systems_Main.resize(650, 398)
        self.centralwidget = QtWidgets.QWidget(Number_Systems_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_output.setGeometry(QtCore.QRect(390, 30, 251, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_output.sizePolicy().hasHeightForWidth())
        self.textBrowser_output.setSizePolicy(sizePolicy)
        self.textBrowser_output.setObjectName("textBrowser_output")
        self.btn_save_text = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_text.setGeometry(QtCore.QRect(500, 250, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_text.sizePolicy().hasHeightForWidth())
        self.btn_save_text.setSizePolicy(sizePolicy)
        self.btn_save_text.setObjectName("btn_save_text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 0, 241, 31))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 250, 101, 31))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 251, 31))
        self.label_11.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.textBrowser_input = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_input.setGeometry(QtCore.QRect(10, 30, 251, 211))
        self.textBrowser_input.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.textBrowser_input.setObjectName("textBrowser_input")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 101, 31))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.btn_load_text = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_text.setGeometry(QtCore.QRect(120, 250, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_load_text.sizePolicy().hasHeightForWidth())
        self.btn_load_text.setSizePolicy(sizePolicy)
        self.btn_load_text.setObjectName("btn_load_text")
        self.btn_code = QtWidgets.QPushButton(self.centralwidget)
        self.btn_code.setGeometry(QtCore.QRect(270, 110, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_code.sizePolicy().hasHeightForWidth())
        self.btn_code.setSizePolicy(sizePolicy)
        self.btn_code.setObjectName("btn_code")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(10, 330, 631, 31))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.type_radix = QtWidgets.QComboBox(self.centralwidget)
        self.type_radix.setGeometry(QtCore.QRect(270, 290, 41, 31))
        self.type_radix.setObjectName("type_radix")
        self.type_radix.addItem("")
        self.type_radix.addItem("")
        self.type_radix.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 290, 241, 31))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.rb_encode = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_encode.setGeometry(QtCore.QRect(330, 290, 16, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_encode.sizePolicy().hasHeightForWidth())
        self.rb_encode.setSizePolicy(sizePolicy)
        self.rb_encode.setText("")
        self.rb_encode.setObjectName("rb_encode")
        self.buttonGroup = QtWidgets.QButtonGroup(Number_Systems_Main)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rb_encode)
        self.rb_decode = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_decode.setGeometry(QtCore.QRect(480, 290, 16, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_decode.sizePolicy().hasHeightForWidth())
        self.rb_decode.setSizePolicy(sizePolicy)
        self.rb_decode.setText("")
        self.rb_decode.setObjectName("rb_decode")
        self.buttonGroup.addButton(self.rb_decode)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 290, 71, 31))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 290, 91, 31))
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(-4, -8, 661, 391))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("background.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.textBrowser_output.raise_()
        self.btn_save_text.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_11.raise_()
        self.textBrowser_input.raise_()
        self.label_3.raise_()
        self.btn_load_text.raise_()
        self.btn_code.raise_()
        self.label_error.raise_()
        self.type_radix.raise_()
        self.label.raise_()
        self.rb_encode.raise_()
        self.rb_decode.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        Number_Systems_Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Number_Systems_Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Number_Systems_Main.setMenuBar(self.menubar)
        self.info = QtWidgets.QAction(Number_Systems_Main)
        self.info.setObjectName("info")
        self.help = QtWidgets.QAction(Number_Systems_Main)
        self.help.setObjectName("help")
        self.history = QtWidgets.QAction(Number_Systems_Main)
        self.history.setObjectName("history")
        self.menu.addAction(self.info)
        self.menu.addAction(self.help)
        self.menu.addAction(self.history)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Number_Systems_Main)
        QtCore.QMetaObject.connectSlotsByName(Number_Systems_Main)

    def retranslateUi(self, Number_Systems_Main):
        _translate = QtCore.QCoreApplication.translate
        Number_Systems_Main.setWindowTitle(
            _translate("Number_Systems_Main", "Amgine Number Systems"))
        self.btn_save_text.setText(_translate("Number_Systems_Main", "Сохранить"))
        self.label_2.setText(_translate("Number_Systems_Main",
                                        "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Вывод</span></p></body></html>"))
        self.label_4.setText(_translate("Number_Systems_Main",
                                        "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Сохранить текст</span></p></body></html>"))
        self.label_11.setText(_translate("Number_Systems_Main",
                                         "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Ввод</span></p></body></html>"))
        self.label_3.setText(_translate("Number_Systems_Main",
                                        "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Загрузить текст</span></p></body></html>"))
        self.btn_load_text.setText(_translate("Number_Systems_Main", "Загрузить"))
        self.btn_code.setText(_translate("Number_Systems_Main", "→"))
        self.type_radix.setItemText(0, _translate("Number_Systems_Main", "2"))
        self.type_radix.setItemText(1, _translate("Number_Systems_Main", "8"))
        self.type_radix.setItemText(2, _translate("Number_Systems_Main", "16"))
        self.label.setText(_translate("Number_Systems_Main",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Выберите основание системы счисления</span></p></body></html>"))
        self.label_5.setText(_translate("Number_Systems_Main",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">Зашифровать</span></p></body></html>"))
        self.label_6.setText(_translate("Number_Systems_Main",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">Дешифровать</span></p></body></html>"))
        self.menu.setTitle(_translate("Number_Systems_Main", "Меню"))
        self.info.setText(_translate("Number_Systems_Main", "Инфо"))
        self.help.setText(_translate("Number_Systems_Main", "Помощь"))
        self.history.setText(_translate("Number_Systems_Main", "История"))
