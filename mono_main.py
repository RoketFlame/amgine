from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mono_Alpha_Main(object):
    def setupUi(self, Mono_Alpha_Main):
        Mono_Alpha_Main.setObjectName("Mono_Alpha_Main")
        Mono_Alpha_Main.resize(422, 139)
        self.centralwidget = QtWidgets.QWidget(Mono_Alpha_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add_dict = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_dict.setGeometry(QtCore.QRect(10, 50, 181, 41))
        self.btn_add_dict.setObjectName("btn_add_dict")
        self.btn_use_dict = QtWidgets.QPushButton(self.centralwidget)
        self.btn_use_dict.setGeometry(QtCore.QRect(230, 50, 181, 41))
        self.btn_use_dict.setObjectName("btn_use_dict")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 111, 20))
        self.label.setObjectName("label")
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
        self.label.setText(_translate("Mono_Alpha_Main", "<html><head/><body><p align=\"center\">Выберете функцию</p></body></html>"))
