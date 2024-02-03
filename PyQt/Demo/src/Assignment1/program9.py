'''
9. Create a PyQt window with a proress bar .Implement a function that simulates a task(eg.,File download) and
updates the progress bar accordingly
'''
import urllib.request
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys

from PyQt5.QtWidgets import QWidget

class Progressar(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(25,45,210,30)
        self.button = QPushButton('Start',self)
        self.button.move(50,100)
        self.button.clicked.connect(self.Download)
        self.setGeometry(301,310,400,200)
        self.setWindowTitle("ProgressBar")
    
    def Handle_Progress(self,blocknum,blocksize,totalsize):
        readed_data = blocknum*blocksize
        if totalsize>0:
            dowload_percentage  = readed_data*100/totalsize
            self.progressBar.setValue(int(dowload_percentage))
            QApplication.processEvents()

    def Download(self):
        down_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwallpapers.com%2Fjai-shree-ram-hd&psig=AOvVaw1QMn_SsDhNW5FPXN8j4e19&ust=1706020931628000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCLDY7NCd8YMDFQAAAAAdAAAAABAI'

        save_loc = 'C:/WIN10/Desktop/Python_Projects/Demo/assets/images/images.jpg'

        urllib.request.urlretrieve(down_url,save_loc,self.Handle_Progress)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Progressar()
    window.show()
    sys.exit(app.exec_())
