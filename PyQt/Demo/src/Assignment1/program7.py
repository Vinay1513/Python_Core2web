'''
7. Design a PyQt window that includes a QSlider and a QLael.Update te Label text dynamically to reflect the 
current value of the slider 
'''



import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout,QSlider

class SliderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider App")
        self.setGeometry(100,100,400,200)
        self.setStyleSheet("background:lightblue")

        layout=QVBoxLayout()

        #Create a QSlider widget
        self.slider = QSlider(Qt.Horizontal,self)
        layout.addWidget(self.slider)

        #create a Qlabel widget
        self.label=QLabel("Slider Value: 0",self)
        layout.addWidget(self.label)

        self.slider.valueChanged.connect(self.update_label)
        self.setLayout(layout)

    def update_label(self):
        value = self.slider.value()
        self.label.setText(f"Slider Value is  : {value}")
        self.setStyleSheet("background:pink")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SliderApp()
    window.show()
    sys.exit(app.exec_())
