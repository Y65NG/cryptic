import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QToolTip, QHBoxLayout, QVBoxLayout, QTextEdit, QInputDialog
# from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from cryptic import *
import imp

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    

    def initUI(self):
        
        self.key = QLabel('Key')
        self.text = QLabel('Text')
        self.review = QLabel('Review')
 
        self.keyEdit = QLineEdit(self)
        self.textEdit = QLineEdit(self)
        self.answer = QPushButton('Result')
        self.answerEdit = QLineEdit(self)
 
        grid = QGridLayout()
        grid.setSpacing(10)
 
        grid.addWidget(self.key, 1, 0)
        grid.addWidget(self.keyEdit, 1, 1)
 
        grid.addWidget(self.text, 2, 0)
        grid.addWidget(self.textEdit, 2, 1)
        
        grid.addWidget(self.answer, 3, 0)
        grid.addWidget(self.answerEdit, 3, 1)
        self.answer.clicked.connect(self.buttonClicked)
 
        # grid.addWidget(review, 3, 0)
        # grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()

    def buttonClicked(self):
        text = self.textEdit.text()
        key = int(self.keyEdit.text())
        tables = read_table('matchs.csv')
        # print(text, key)
        self.answerEdit.setText(encrypt(text, tables, key, 100))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    
    sys.exit(app.exec_())