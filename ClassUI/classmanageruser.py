"""
航班管理员用户GUI界面以及相关操作
"""
from UI.ManageuserUI import *
from ClassUI.classlogin import *
from PyQt5.QtWidgets import QPushButton, QTableWidgetItem, QApplication, QMainWindow, QMessageBox
import sys
import config


class ManageruserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ManageruserWindow()
        self.ui.setupUi(self)
        self.login_win = None
        self.original_flight_number = None
        # 隐藏外部窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_changepass.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_search_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButtonBack_tosearch.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        self.ui.pushButton_5.clicked.connect(self.change_pass)
        self.ui.pushButton_Logout.clicked.connect(self.log_out)

        self.ui.pushButton_add.clicked.connect(self.add_flight)
        self.ui.pushButton_8.clicked.connect(self.edit_confirm)
        self.ui.pushButton_search.clicked.connect(self.msearch_flights)

        self.ui.pushButton_all.clicked.connect(self.show_all_flights)
        self.ui.pushButton_shai.clicked.connect(self.shaixuan)

        # 页面显示
        self.show()

    def change_pass(self):
        new_pass1 = self.ui.lineEdit_U_pass_1.text()
        new_pass2 = self.ui.lineEdit_U_pass_2.text()
        if len(new_pass1) == 0 or len(new_pass2) == 0:
            self.ui.stackedWidget_2.setCurrentIndex(1)
        elif new_pass1 == new_pass2:
            sql.reset_password_in_file(config.user_now, new_pass1, config.file_path_managers)
            self.ui.stackedWidget_2.setCurrentIndex(3)

        else:
            self.ui.stackedWidget_2.setCurrentIndex(2)

    def log_out(self):
        config.user_now = ''
        self.close()
        from ClassUI.classlogin import LoginWindow  # 动态引入类
        self.login_win = LoginWindow()

    def add_flight(self):
        flight_number = self.ui.lineEditCode.text()
        departure = self.ui.lineEditLau.text()
        arrival = self.ui.lineEditArr.text()
        schedule = self.ui.lineEditDate_3.text()
        departure_time = self.ui.lineEditLauTime.text()
        arrival_time = self.ui.lineEditArrTime.text()
        available_tickets = self.ui.lineEditNumber.text()
        price = self.ui.lineEditPrice1.text()
        flag = sql.check_exists(flight_number, config.file_path_flights)
        if not flight_number or not departure or not arrival or not schedule or not departure_time or not arrival_time or not price or not available_tickets:
            self.ui.stackedWidget_3.setCurrentIndex(2)
        elif flag:
            self.ui.stackedWidget_3.setCurrentIndex(3)
        else:
            new_flight_info = f"\n{flight_number},{departure},{arrival},{schedule},{departure_time},{arrival_time},{available_tickets},{price}"
            sql.add_flight_in_file(new_flight_info, config.file_path_flights)
            self.ui.stackedWidget_3.setCurrentIndex(1)

    def msearch_flights(self):
        """管理员查找航班"""
        chu = self.ui.lineEditChu.text()
        dao = self.ui.lineEditDao.text()
        date = self.ui.comboBox_2.currentText()
        if not chu and not dao and not date:
            self.ui.stackedWidget_4.setCurrentIndex(2)
            return
        # results是列表，采用顺序表存放航班信息
        results = sql.search_flights_in_file(chu, dao, date, config.file_path_flights)
        if not len(results):
            self.ui.stackedWidget_4.setCurrentIndex(1)
        else:
            self.ui.stackedWidget_4.setCurrentIndex(3)

        self.ui.tableWidget.setRowCount(len(results))
        for row_index, row_data in enumerate(results):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row_index, col_index, item)
                pbtn1 = QPushButton("修改")
                pbtn2 = QPushButton("删除")
                # 这里不可以直接写成self.book_ticket(row_index)
                pbtn1.clicked.connect(lambda _, r=row_index: self.edit_page(r))
                self.ui.tableWidget.setCellWidget(row_index, 8, pbtn1)
                pbtn2.clicked.connect(lambda _, r=row_index: self.delete_flights(r))
                self.ui.tableWidget.setCellWidget(row_index, 9, pbtn2)

    def edit_page(self, row):
        """修改页面"""
        self.ui.stackedWidget.setCurrentIndex(3)
        self.original_flight_number = self.ui.tableWidget.item(row, 0).text()
        departure = self.ui.tableWidget.item(row, 1).text()
        arrival = self.ui.tableWidget.item(row, 2).text()
        schedule = self.ui.tableWidget.item(row, 3).text()
        departure_time = self.ui.tableWidget.item(row, 4).text()
        arrival_time = self.ui.tableWidget.item(row, 5).text()
        available_tickets = self.ui.tableWidget.item(row, 6).text()
        price = self.ui.tableWidget.item(row, 7).text()
        self.ui.lineEditDate_4.setText(schedule)
        self.ui.lineEditCode_2.setText(self.original_flight_number)
        self.ui.lineEditLauTime_2.setText(departure_time)
        self.ui.lineEditArrTime_2.setText(arrival_time)
        self.ui.lineEditArr_2.setText(arrival)
        self.ui.lineEditLau_2.setText(departure)
        self.ui.lineEditPrice1_2.setText(price)
        self.ui.lineEditNumber_2.setText(available_tickets)

    def edit_confirm(self):
        """修改航班信息"""
        flight_number = self.ui.lineEditCode_2.text()
        departure = self.ui.lineEditLau_2.text()
        arrival = self.ui.lineEditArr_2.text()
        schedule = self.ui.lineEditDate_4.text()
        departure_time = self.ui.lineEditLauTime_2.text()
        arrival_time = self.ui.lineEditArrTime_2.text()
        available_tickets = self.ui.lineEditNumber_2.text()
        price = self.ui.lineEditPrice1_2.text()
        flag = sql.check_exists(flight_number, config.file_path_flights)
        if not flight_number or not departure or not arrival or not schedule or not departure_time or not arrival_time or not price or not available_tickets:
            self.ui.stackedWidget_5.setCurrentIndex(2)

        elif self.original_flight_number != flight_number and flag:
            self.ui.stackedWidget_5.setCurrentIndex(3)
        else:
            new_flight_info = f"{flight_number},{departure},{arrival},{schedule},{departure_time},{arrival_time},{available_tickets},{price}"
            sql.update_flight_in_file(self.original_flight_number, new_flight_info, config.file_path_flights)
            # 更新机票信息
            sql.update_ticket_flight_number(self.original_flight_number, config.file_path_tickets)
            self.ui.stackedWidget_5.setCurrentIndex(1)

    def delete_flights(self, row):
        """删除航班信息"""
        flight_number = self.ui.tableWidget.item(row, 0).text()
        result = sql.delete_from_file(flight_number, config.file_path_flights)
        # 用户订了该航班的机票也要删除
        result2 = sql.delete_from_file(flight_number, config.file_path_tickets)
        if result and result2:
            QMessageBox.information(self, '成功', '删除成功')
            # 刷新表格或执行其他必要的清理工作
            self.msearch_flights()  # 刷新表格的函数

    def show_all_flights(self):
        results = sql.read_all(config.file_path_flights)
        self.ui.tableWidget.setRowCount(len(results))
        for row_index, row_data in enumerate(results):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row_index, col_index, item)
                pbtn1 = QPushButton("修改")
                pbtn2 = QPushButton("删除")
                pbtn1.clicked.connect(lambda _, r=row_index: self.edit_page(r))
                self.ui.tableWidget.setCellWidget(row_index, 8, pbtn1)
                pbtn2.clicked.connect(lambda _, r=row_index: self.delete_flights(r))
                self.ui.tableWidget.setCellWidget(row_index, 9, pbtn2)

    def shaixuan(self):
        """筛选"""
        choose = self.ui.comboBox.currentText()
        text = self.ui.lineEdit.text()
        chu = self.ui.lineEditChu.text()
        dao = self.ui.lineEditDao.text()
        date = self.ui.comboBox_2.currentText()
        if not text:
            self.ui.stackedWidget_4.setCurrentIndex(2)
            return
        results = sql.filter_flights_in_file(choose, text, chu, dao, date, config.file_path_flights)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(results))
        if not len(results):
            self.ui.stackedWidget_4.setCurrentIndex(1)
        else:
            self.ui.stackedWidget_4.setCurrentIndex(3)
        for row_index, row_data in enumerate(results):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row_index, col_index, item)
                pbtn1 = QPushButton("修改")
                pbtn2 = QPushButton("删除")
                pbtn1.clicked.connect(lambda _, r=row_index: self.edit_page(r))
                self.ui.tableWidget.setCellWidget(row_index, 8, pbtn1)
                pbtn2.clicked.connect(lambda _, r=row_index: self.delete_flights(r))
                self.ui.tableWidget.setCellWidget(row_index, 9, pbtn2)


"""用于调试用"""
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = ManageruserWindow()
    sys.exit(app.exec_())
