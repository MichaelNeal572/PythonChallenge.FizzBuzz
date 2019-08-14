# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 471, 231))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.lstRules = QtWidgets.QListView(self.groupBox)
        self.lstRules.setGeometry(QtCore.QRect(10, 20, 211, 201))
        self.lstRules.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lstRules.setObjectName("lstRules")
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnRemove = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout.addWidget(self.btnRemove)
        self.spnMaxNum = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spnMaxNum.setObjectName("spnMaxNum")
        self.spnMaxNum.setMinimum(1)
        self.spnMaxNum.setMaximum(999)
        self.verticalLayout.addWidget(self.spnMaxNum)
        self.btnPlay = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnPlay.setObjectName("btnPlay")
        self.verticalLayout.addWidget(self.btnPlay)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 250, 481, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.txteOut = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.txteOut.setGeometry(QtCore.QRect(10, 20, 461, 231))
        self.txteOut.setObjectName("txteOut")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fizz Buzz"))
        self.groupBox.setTitle(_translate("MainWindow", "Rules"))
        self.btnAdd.setText(_translate("MainWindow", "Add Rule"))
        self.btnRemove.setText(_translate("MainWindow", "Remove Rule"))
        self.btnPlay.setText(_translate("MainWindow", "Play!"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

