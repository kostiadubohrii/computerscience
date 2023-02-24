import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
win1 = uic.loadUiType("miles_calc.ui")[0]

 

class WindowClass(QtWidgets.QMainWindow, win1): ## inhertiene
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self, parent) ## constructor for the super model
        self.setupUi(self);self.txtInput.setVisible(True);
        self.RdoMiles.setChecked(True);self.RdoKm.setChecked(False)
        self.BtnCalculate.clicked.connect(self.calculation)
    # def validate(value):
        
    
    def calculation(self):
        strvalue=self.txtInput.text(); output=""
        fltvalue=float(strvalue)
        if self.RdoMiles.isChecked()==True:
            result=fltvalue/1.61;output="The value in miles ";
        elif self.RdoKm.isChecked()==True:
            result=fltvalue*1.61;output="the value in km is "
        result=round(result,2)
        self.lblOutput.setText(output+str(result))
        self.txtInput.setText(" ")
app = QtWidgets.QApplication(sys.argv)
myWindow = WindowClass(None) ## set the balue of our First window
myWindow.show() ## makes it show    
app.exec_()    