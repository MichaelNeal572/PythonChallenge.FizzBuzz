# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Learning\Python\Fizz_buzz\newRuleUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(283, 169)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.leTo = QtWidgets.QLineEdit(self.centralwidget)
        self.leTo.setGeometry(QtCore.QRect(100, 50, 151, 20))
        self.leTo.setObjectName("leTo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 47, 13))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(60, 90, 75, 23))
        self.btnOK.setObjectName("btnOK")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.btnCancel.setObjectName("btnCancel")
        self.spnChange = QtWidgets.QSpinBox(self.centralwidget)
        self.spnChange.setGeometry(QtCore.QRect(100, 20, 151, 22))
        self.spnChange.setObjectName("spnChange")
        self.spnChange.setMinimum(1)
        self.spnChange.setMaximum(999)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 283, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New Rule"))
        self.label_2.setText(_translate("MainWindow", "To: "))
        self.label.setText(_translate("MainWindow", "Change: "))
        self.btnOK.setText(_translate("MainWindow", "OK"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

