from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Ui_Dialog):
        Ui_Dialog.setObjectName("Ui_Dialog")
        Ui_Dialog.resize(411, 148)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Ui_Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 331, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.label = QtWidgets.QLabel(Ui_Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 331, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Ui_Dialog)
        self.buttonBox.accepted.connect(Ui_Dialog.accept)
        self.buttonBox.rejected.connect(Ui_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Ui_Dialog)

    def retranslateUi(self, Ui_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Ui_Dialog.setWindowTitle('Amgine')
        self.label.setText(_translate("Ui_Dialog",
                                      "<html><head/><body><p><span style=\" font-size:11pt;\">Введите логин</span></p></body></html>"))
