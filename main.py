import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QAction, QMenu, QFrame) #Imports indicados por su nombre
from PyQt5.QtGui import QFont, QPainter, QColor
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
        self.status = self.statusBar()
        self.initUi()
        self.show()

    def initUi(self):
        self.setCentralWidget(self.frame)

        self.status.showMessage("Score:0")
        self.title_label.setGeometry(0,0,500,20)
        self.title_label.setStyleSheet("background-color: black;"
                                  "color: blue;")
        self.title_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.frame.setGeometry(0,20,500,450) #Created frame in which snake will move
        self.frame.setStyleSheet("background-color: green;")
        


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
#Code that managues the movement line 42-50
        
        
class Grid (QFrame): #Created the class so i can override some specific methods i need for my snake widget
    def __init__(self):
        super().__init__()
        self.snake =[(5,5), (5,6), (5,7)] #Initial snake position
        self.food = (10,10) #Initial food position 
        self.timer = QTimer(self) #Just creates the timer object
        self.timer.timeout.connect(self.update_game) #Calls update game on every timeout
        self.timer.start(100) #triggers every 100ms to control game speed
        self.direction = "RIGHT"  # Default direction when the game starts

    def paintEvent(self, event):
        painter = QPainter(self) #QPainter allows us to draw on the window, in this case inside our frame
        painter.setBrush(QColor(102,255,178))

        for x, y in self.snake:
            painter.drawRect(x*20, y*20,20,20)
        
        painter.setBrush(QColor(255,0,0)) #This paints the food (250) = red, funtion works for RGB
        painter.drawRect(self.food[0] * 20, self.food[1] *20,20,20) #Draws food

        
    def change_direction(self, new_direction):
        opposite_directions = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_direction != opposite_directions.get(self.direction):  
            self.direction = new_direction

    def update_game(self):
        self.update()
#Aquitecture for the game loop starting from self.timer 
    def check_collision(self):
        head_x, head_y = self.snake[0]  # Get snake's head position

        # Check if the snake hits the wall
        if head_x < 0 or head_x >= 25 or head_y < 0 or head_y >= 20:
            self.timer.stop()  # Stop the game

        # Check if the snake collides with itself
        if (head_x, head_y) in self.snake[1:]:
            self.timer.stop()  # Stop the game

    def update_game(self):
        head_x, head_y = self.snake[0]  # Get current head position

        # Move the head in the current direction
        if self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1
        elif self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1

        new_head = (head_x, head_y)  # Create new head position

        # Check if the snake eats food
        if new_head == self.food:
            self.snake.insert(0, new_head)  # Grow the snake
            self.food = (random.randint(0, 24), random.randint(0, 19))  # New food position
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()  # Remove the tail (to keep the same length)

        self.check_collision()  # Check if the game should end
        self.update()  # Redraw the screen




app = QApplication(sys.argv) #Manages the start of an app
window = MainWindow()
window.show()
sys.exit(app.exec_())
