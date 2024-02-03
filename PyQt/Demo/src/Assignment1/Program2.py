'''
2. Design a PyQt window with a QpushButton and QLabl.Upob clicking the button change the text of QLabel to "Button Clicked!"
'''
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout,QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("main window")
        self.setGeometry(500,300,500,300)
        self.mainLayout=QVBoxLayout(self)
        self.mainLayout.setSpacing(0)
        self.setLayout(self.mainLayout)

        self.label1=QLabel("Hello core2wb")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setFixedSize(500,30)
        self.mainLayout.addWidget(self.label1,alignment=Qt.AlignmentFlag.AlignCenter)
        self.addButton()
    
    def addButton(self):
        self.Button1 = QPushButton("Text change")
        self.Button1.setFixedSize(100,30)
        self.Button1.clicked.connect(lambda:self.label1.setText("Hello Core2web" if self.label1.text() == "I am Here" else "I am Here"))
        self.mainLayout.addWidget(self.Button1,alignment=Qt.AlignmentFlag.AlignCenter)

if __name__=="__main__":
    app=QApplication(sys.argv)
    main_window=MainWindow()
    main_window.show()
    sys.exit(app.exec_())