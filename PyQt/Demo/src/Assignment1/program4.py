'''
4. Implement a PyQt dialog box that promts users to enetr their names using a QLineEdit.
Upon clicking "OK" display a QmessegeBox with personalized greeting.
'''

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QComboBox,QLabel,QLineEdit,QPushButton,QMessageBox


class UserDialogBox(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # create a QvBoxLayout
        layout=QVBoxLayout()
        self.setStyleSheet("background:orange")
        label = QLabel("Enter your Name")
        layout.addWidget(label)

        #QLineEdit for entering userName
        self.user_input = QLineEdit()
        self.user_input.setStyleSheet("background:yellow")
        layout.addWidget(self.user_input)
      

        button = QPushButton("Ok")
     
        button.setStyleSheet("background:lightblue")
        button.clicked.connect(self.show_messege)
        layout.addWidget(button)
        self.setLayout(layout)

    def show_messege(self):
        
        username = self.user_input.text()
        if username:
            QMessageBox.information(self,"UserName",f"Your name is:{username}")
        else:
            QMessageBox.warning(self,"warning","Please enter a username.")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog= UserDialogBox()
    dialog.setWindowTitle("UserName Dialog Box")
    dialog.setGeometry(200,100,500,300)
    dialog.show()
    sys.exit(app.exec_())
