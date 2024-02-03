'''
6. Build a PyQt application with a QRadioButton group for selection a programming language
(e.g,Python,Java,c++).Display a messege indicating the selected language when a radio button is clicked
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout,QRadioButton


class RadioButtonApp(QWidget):
    def __init__(self):
        super().__init__()

        self.radioUI()
    def radioUI(self):
        self.setWindowTitle("Radio Button Example")
        self.setGeometry(300,300,400,200)
        self.setStyleSheet("background:lightblue")
        layout=QVBoxLayout()

        #create radio buttons for options
        self.option1_radio = QRadioButton("Python",self)
        self.option2_radio=QRadioButton("Java",self)
        self.option3_radio=QRadioButton("C++",self)


        layout.addWidget(self.option1_radio)
        layout.addWidget(self.option2_radio)
        layout.addWidget(self.option3_radio)

        #create a label to display the selected option
        self.selected_option_label = QLabel("Selected Option:None",self)
        layout.addWidget(self.selected_option_label)

        #connect the radio buttons' toggled signal to a slot that updates the label
        self.option1_radio.toggled.connect(lambda:self.update_selected_option("Python"))
        self.option2_radio.toggled.connect(lambda:self.update_selected_option("Java"))
        self.option3_radio.toggled.connect(lambda:self.update_selected_option("C++"))

        self.setLayout(layout)
    def update_selected_option(self,option):
        if option:
            self.selected_option_label.setText(f"Selected Option:{option}")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RadioButtonApp()
    window.show()
    sys.exit(app.exec_())