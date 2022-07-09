from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

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
        self.ui.pushButton_2.clicked.connect(self.button_search_ktru)

    def show_rzn_items(self):
        self.search_rzn = self.ui.lineEdit.text()
        self.rzn_list = self.search_class.ros_zdrav_list_search(self.search_rzn, int(self.ui.comboBox.currentText()))
        self.ui.label_3.setText(str(self.rzn_list[0]))
        for co,it in enumerate(self.rzn_list[1::]):
            self.ui.tableWidget.setRowCount(co+1)
            if 'name_full' in it:
                self.ui.tableWidget.setItem(co, 0, QTableWidgetItem(f"{it['name_full']}"))
            else:
                self.ui.tableWidget.setItem(co, 0, QTableWidgetItem(f"{it['name_short']}"))

            self.ui.tableWidget.setItem(co, 1, QTableWidgetItem(f"{it['nkmi']}"))

    def button_search_ktru(self):
        # id = self.rzn_list[ret.row() + 1]['id']
        ret = self.ui.tableWidget.currentItem()
        if ret.text().isdigit and len(ret.text()) == 6:
            resp = self.search_class.search_ktru_by_nkmi(ret.text())
            if resp == None:
                QMessageBox.critical(self, "Ошибка поиска",
                                     "КТРУ не существует",
                                     QMessageBox.Ok)
            else:
                ls_ktru = self.search_class.search_ktrus(resp)
                for co, it in enumerate(ls_ktru):
                    self.ui.tableWidget_2.setRowCount(co + 1)
                    self.ui.tableWidget_2.setItem(co, 0, QTableWidgetItem(f"{it[0]}"))
                    self.ui.tableWidget_2.setItem(co, 1, QTableWidgetItem(f"{it[1]}"))
                    self.ui.tableWidget_2.setItem(co, 2, QTableWidgetItem(f"{it[2]}"))

        elif ret.text() == 'см. приложение':
            print('приложение')


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())