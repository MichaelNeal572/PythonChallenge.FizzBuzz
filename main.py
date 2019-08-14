import newRuleUI as newRuleUI
import homeUI as homeUI
import Fizz_Buzz as fb
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

'''
from pprint import pprint
pprint(vars(home.ui))
'''

class GUI_home:
    def __init__(self):
        self.app = homeUI.QtWidgets.QApplication(sys.argv)
        self.MainWindow = homeUI.QtWidgets.QMainWindow()
        self.ui = homeUI.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.connect_buttons()
        self.reset_rule_display()
        self.update_rule_display()
        
    def connect_buttons(self):
        self.ui.btnAdd.clicked.connect(self.open_newrule)
        self.ui.btnPlay.clicked.connect(self.play)
        self.ui.btnRemove.clicked.connect(self.remove_rule)
    
    def reset_rule_display(self):
        self.model = QtGui.QStandardItemModel()
        self.ui.lstRules.setModel(self.model)
    
    def update_rule_display(self):
        self.rules = game.get_rules()
        self.model = QtGui.QStandardItemModel()
        for key, value in sorted(self.rules.items()):
            self.item = QtGui.QStandardItem(str(key) +" - "+ str(value))
            self.model.appendRow(self.item)
        self.ui.lstRules.setModel(self.model)
            
    def open_newrule(self):
        newrule.open_window()
        
    def remove_rule(self):
        try:
            num = self.ui.lstRules.selectedIndexes()
            game.remove_rule(num[0].data().split(" - ")[0])
            self.update_rule_display()
        except(Exception):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("No Rule Selected")
            msg.setInformativeText('Please select a rule from the list to remove')
            msg.setWindowTitle("Error")
            msg.exec_()
        
    def play(self):
        game.set_maxnum(self.ui.spnMaxNum.value())
        self.ui.txteOut.setPlainText(game.play_GUI())
    
    def open_window(self):
        self.MainWindow.show()

class GUI_newrule:
    def __init__(self):
        self.app = newRuleUI.QtWidgets.QApplication(sys.argv)
        self.MainWindow = newRuleUI.QtWidgets.QMainWindow()
        self.ui = newRuleUI.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.connect_buttons()
        
    def connect_buttons(self):
        self.ui.btnOK.clicked.connect(self.add_rule)
        self.ui.btnCancel.clicked.connect(self.close_window)
    
    def add_rule(self):
        if(self.ui.leTo.text()!=""):
            game.add_rule(self.ui.spnChange.value(),self.ui.leTo.text())
            home.update_rule_display()
            self.close_window()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("To: field is blank")
            msg.setInformativeText('Please insert a phrase to make a rule')
            msg.setWindowTitle("Error")
            msg.exec_()
    
    def close_window(self):
        self.MainWindow.hide()
    
    def open_window(self):
        self.MainWindow.show()

if __name__=="__main__":
    game=fb.fizz_buzz()
    home = GUI_home()
    newrule = GUI_newrule()
    home.open_window()
    sys.exit(home.app.exec_())