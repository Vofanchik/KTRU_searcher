from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from User_inface import Ui_MainWindow
import NkmiSearcher
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.search_class = NkmiSearcher.NkmiSearcher()
        self.ui.pushButton.clicked.connect(self.show_rzn_items)
        # self.ui.tableWidget.resizeColumnsToContents()

    def show_rzn_items(self):
        self.search_rzn = self.ui.lineEdit.text()
        rzn_list = self.search_class.ros_zdrav_list_search(self.search_rzn)
        for co,it in enumerate(rzn_list):
            self.ui.tableWidget.setRowCount(co+1)
            self.ui.tableWidget.setItem(co, 0, QTableWidgetItem(f"{it['name_full']}"))
            self.ui.tableWidget.setItem(co, 1, QTableWidgetItem(f"{it['nkmi']}"))



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())