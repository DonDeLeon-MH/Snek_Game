import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QAction, QMenu, QFrame) #Imports indicados por su nombre
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
import random


class MainWindow(QMainWindow): #Inheritance from QMainWindow, which is a framework class gives you all main functions
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.setWindowTitle("Snek")
        self.setWindowIcon(QtGui.QIcon("./image/image.png"))
        self.title_label = QLabel("Snake Game", self)
        self.frame = Grid()
        self.score = self.statusBar().showMessage("Score:")
        self.initUi()
        self.show()

    def initUi(self):
        self.setCentralWidget(self.frame)

        
        self.title_label.setGeometry(0,0,500,20)
        self.title_label.setStyleSheet("background-color: black;"
                                  "color: blue;")
        self.title_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.frame.setGeometry(0,20,500,450) #Created frame in which snake will move
        self.frame.setStyleSheet("background-color: green;")
        self.frame.timer.setInterval(100) #Refreshes the frame every 100 ms, for snakes movement
        


        vbox = QVBoxLayout()

        vbox.addWidget(self.title_label)
        vbox.addWidget(self.frame)

    def keyPressEvent(self, event): #Function called each time a key is pressed 
        if event.key() == Qt.Key_W:  #Check what was the key that was pressed, and assign it to the event.key() var
            self.frame.change_direction("UP") #calls a method already in grid method to change the direction of the snek
        if event.key() == Qt.Key_A:
            self.frame.change_direction("LEFT")
        if event.key() == Qt.Key_D:
            self.frame.change_direction("RIGHT")
        if event.key() == Qt.Key_S:
            self.frame.change_direction("DOWN")

        
        
class Grid (QFrame): #Created the class so i can override some specific methods i need for my snake widget
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self) #Just creates the timer object
        self.timer.timeout.connect(self.update_game) #Calls update game on every timeout
        self.timer.start(100) #triggers every 100ms to control game speed

    def update_game(self):
        self.update()
#Aquitecture for the game loop in PyQt5 line 45-52
    def fruit_spawn(self):
        fruit = QtGui.QPainter




app = QApplication(sys.argv) #Manages the start of an app
window = MainWindow()
window.show()
sys.exit(app.exec_())
