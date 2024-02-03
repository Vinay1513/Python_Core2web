
'''
3. Develop a PyQt application with a QmainWindow that contains a QmenuBar.Includes at least two menus with corresponding actions,and
displaying appropriate messeges wen actions are triggered.
'''
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox,QAction


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyqt menu example")
        self.setGeometry(500,100,500,300)
        self.setStyleSheet("background:lightblue")
        self.create_menus()
    def create_menus(self):
        menubar=self.menuBar()
        

        #Filemenu
        file_menu=menubar.addMenu("File")
        open_action = QAction("open",self)
        file_menu.setStyleSheet("background:grey")
        open_action.triggered.connect(self.show_messege_open)
        file_menu.addAction(open_action)

        exit_action=QAction("Exit",self)
        exit_action.triggered.connect(self.show_messege_exit)
        file_menu.addAction(exit_action)

        #Edit menu
        edit_menu=menubar.addMenu("Edit")
        cut_Action=QAction("cut",self)
        edit_menu.setStyleSheet("background:grey")
        cut_Action.triggered.connect(self.show_messege_cut)
        edit_menu.addAction(cut_Action)

        copy_action=QAction("copy",self)
        copy_action.triggered.connect(self.show_messege_copy)
        edit_menu.addAction(copy_action)

    def show_messege_open(self):
        QMessageBox.information(self,"Open Action","Open action triggered")
    
    def show_messege_exit(self):
        QMessageBox.information(self,"Exit Action","Exit action triggered")

    def show_messege_cut(self):
        QMessageBox.information(self,"Cut Action","Cut action triggered")

    def show_messege_copy(self):
        QMessageBox.information(self,"Copy Action","Copy action triggered")
if __name__ == "__main__":
    app=QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())        
        
