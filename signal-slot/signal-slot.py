#!/use/bin/python3A
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def MyApp():
    app = QApplication(sys.argv)
    window = QDialog()
   

    b1 = QPushButton(window)
    b1.setText("Button1")
    b1.move(200, 250)
    b1.clicked.connect(b1_clicked)
    
    clr = QPushButton(window)
    clr.setText("Clear")
    clr.move(200, 300)
    clr.clicked.connect(clr_clicked)
    
    b2 = QPushButton(window)
    b2.setText("Button2")
    b2.move(200, 350)
    b2.clicked.connect(b2_clicked)

    global l1
    l1 = QLabel(window)
    l1.setText("QLable is empty")
    l1.move(200, 450)

    
    window.setGeometry(500,500,500,500)

    window.show();
    sys.exit(app.exec())

def b1_clicked():
    l1.setText("QPushButton b1 clicked")
    print("QPushButton b1 clicked\n");

def clr_clicked():
    l1.setText("")
    print("QPushButton Clear clicked\n");

def b2_clicked():
    l1.setText("QPushButton b2 clicked")
    print("QPushButton b2 clicked\n");

if __name__ == '__main__':
    MyApp()
