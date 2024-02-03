'''
8. Dvelop a simple PyQt application with a QTableWidget diplaying a rid of data('eg.numers or names)
'''


import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore,QtGui,QtWidgets

class TabelModel(QtCore.QAbstractTableModel):
    def __init__(self,data):
        super(TabelModel,self).__init__()
        self._data = data


    def data(self,index,role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        
    def rowCount(self,index):

        return len(self._data)
    
    def  columnCount(self,index):
        return len(self._data[0])
    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()
        data = [
            [4,9,2],
            [1,0,0],
            [3,5,0],
            [3,3,2],
            [7,8,9]
        ]
        self.model = TabelModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

