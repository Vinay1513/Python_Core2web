'''
10. Build a PyQt application with a QTabWidget containing multiple tabs.Each tab should have different
content,such as text,buttons,or images
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Example")
        self.setGeometry(300,300,400,200)
        self.setStyleSheet("background:grey")

        layout = QHBoxLayout(self)
        


        layout.addWidget(QPushButton("Left-Most"))
        layout.addWidget(QPushButton("Center"),1)
        layout.addWidget(QPushButton("Right-Most"),2)
        

        

        self.setLayout(layout)
        print(self.children())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())