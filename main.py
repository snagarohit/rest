#############################################################
#      NullCon'13 Goa International Security Conference     #
#							    #
#	       ReSt: The REal STealth MITM Tool 	    #
#							    #
#               Copyright (c) 2013 Naga Rohit S             #
#							    #
#     Please find the license agreement of the software     #
#        in the current folder in the file LICENSE.md	    #
#############################################################

import os,sys

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from interface import Ui_widget

# Create a class for our main window
class Main(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        # This is always the same
        self.ui=Ui_widget()
        self.ui.setupUi(self)

def main():
    # Again, this is boilerplate, it's going to be the same on
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
