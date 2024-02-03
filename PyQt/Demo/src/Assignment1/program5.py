'''
5. create a PyQt window with a QComboBox containing  alist of colors.Upon selecting a color.change 
the background color of the window accordingly.
'''
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QComboBox
from PyQt5.QtGui import QColor

class ColorChnagerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # create a QvBoxLayout
        layout=QVBoxLayout()
        #create a QComboBox and add colors to it
        color_combo = QComboBox(self)
        colors=["Red","Green","Blue","Yellow","Cyan","Magenta","Purple"]
        color_combo.addItems(colors)

        #connect the color change signal to the slot
        color_combo.currentIndexChanged.connect(self.change_color)

        layout.addWidget(color_combo)
        self.setLayout(layout)
        #set the intial background color explicitly
        self.change_color(0)

        #set window property
        self.setGeometry(500,300,500,400)
        self.setWindowTitle("Color changer App")

    def change_color(self,index):
        color_name=self.sender().currentText() if self.sender() else "Red"

        color=QColor(color_name)
        self.setStyleSheet(f"background-color:{color.name()};")
if __name__ =='__main__':

    app  = QApplication(sys.argv)
    ex = ColorChnagerApp()
    ex.show()
    sys.exit(app.exec_())


