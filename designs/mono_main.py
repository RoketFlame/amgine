from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mono_Alpha_Main(object):
    def setupUi(self, Mono_Alpha_Main):
        Mono_Alpha_Main.setObjectName("Mono_Alpha_Main")
        Mono_Alpha_Main.resize(422, 119)
        self.centralwidget = QtWidgets.QWidget(Mono_Alpha_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add_dict = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_dict.setGeometry(QtCore.QRect(10, 50, 181, 41))
        self.btn_add_dict.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.btn_add_dict.setObjectName("btn_add_dict")
        self.btn_use_dict = QtWidgets.QPushButton(self.centralwidget)
        self.btn_use_dict.setGeometry(QtCore.QRect(230, 50, 181, 41))
        self.btn_use_dict.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.btn_use_dict.setObjectName("btn_use_dict")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 251, 20))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 431, 121))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.btn_add_dict.raise_()
        self.btn_use_dict.raise_()
        self.label.raise_()
        Mono_Alpha_Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mono_Alpha_Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        Mono_Alpha_Main.setMenuBar(self.menubar)

        self.retranslateUi(Mono_Alpha_Main)
        QtCore.QMetaObject.connectSlotsByName(Mono_Alpha_Main)

    def retranslateUi(self, Mono_Alpha_Main):
        _translate = QtCore.QCoreApplication.translate
        Mono_Alpha_Main.setWindowTitle(_translate("Mono_Alpha_Main", "Amgine"))
        self.btn_add_dict.setText(_translate("Mono_Alpha_Main", "Создать новый алфвит"))
        self.btn_use_dict.setText(_translate("Mono_Alpha_Main", "Использовать уже созданный"))
        self.label.setText(_translate("Mono_Alpha_Main",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Выберете функцию</span></p></body></html>"))
        self.label_2.setText(_translate("Mono_Alpha_Main", "TextLabel"))
