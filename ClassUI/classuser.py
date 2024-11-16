"""
普通用户GUI界面以及相关操作
"""
from UI.UserUI import *
from ClassUI.classlogin import *
from PyQt5.QtWidgets import QPushButton, QTableWidgetItem, QApplication, QMainWindow, QMessageBox
import sys
import config
import sql
from datetime import datetime


class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.all_flights = []
        self.ui = Ui_UserWindow()
        self.ui.setupUi(self)
        self.login_win = None
        # self.his_to_page_buy = []
        # 隐藏外部窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.labelSet2.setText(config.user_now)
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_changepass.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_mytic.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButtonBack_tohome.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_5.clicked.connect(self.change_pass)
        self.ui.pushButton_ULogout.clicked.connect(self.log_out)

        self.ui.pushButton_search.clicked.connect(self.search_flights)
        self.ui.pushButton_7.clicked.connect(self.book_confirm)
        self.ui.pushButton_2.clicked.connect(self.my_tickets)
        self.ui.pushButton_homeshai.clicked.connect(self.homeshai)
        self.ui.pushButton_homeqian.clicked.connect(self.z_price_sort)
        self.ui.pushButton_homedao.clicked.connect(self.z_time_sort)

        # 页面显示
        self.show()

    def change_pass(self):
        """修改密码"""
        new_pass1 = self.ui.lineEdit_U_pass_1.text()
        new_pass2 = self.ui.lineEdit_U_pass_2.text()
        if len(new_pass1) == 0 or len(new_pass2) == 0:
            self.ui.stackedWidget_2.setCurrentIndex(1)
        elif new_pass1 == new_pass2:
            sql.reset_password_in_file(config.user_now, new_pass1, config.file_path_users)
            self.ui.stackedWidget_2.setCurrentIndex(3)
        else:
            self.ui.stackedWidget_2.setCurrentIndex(2)

    # 退出
    def log_out(self):
        """退出登录"""
        config.user_now = ''
        self.close()
        from ClassUI.classlogin import LoginWindow  # 动态引入类
        self.login_win = LoginWindow()

    def search_flights(self):
        """查找航班"""
        chu = self.ui.lineEditChu.text()
        dao = self.ui.lineEditDao.text()
        date = self.ui.comboBox_2.currentText()

        if not chu and not dao and not date:
            self.ui.stackedWidget_3.setCurrentIndex(2)
            return
        # 出发、到达、日期都不为空时，才会搜索所有可能的航班，直达+中转
        if chu and dao and date:
            zhida = sql.search_flights_in_file(chu, dao, date, config.file_path_flights)
            zhongzhuan = sql.find_one_stop_connections(chu, dao, date, config.file_path_flights)
            self.all_flights[:] = zhida + zhongzhuan
            results = zhida
            for line in zhongzhuan:
                results.append(line[:8])
                results.append(line[8:])
        else:
            results = sql.search_flights_in_file(chu, dao, date, config.file_path_flights)
            self.all_flights[:] = results
        if not len(results):
            self.ui.stackedWidget_3.setCurrentIndex(1)
        else:
            self.ui.stackedWidget_3.setCurrentIndex(3)

        self.ui.tableWidget.setRowCount(len(results))
        for row_index, row_data in enumerate(results):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row_index, col_index, item)
                pbtn = QPushButton("订票")
                # 这里不可以直接写成self.book_ticket(row_index)
                pbtn.clicked.connect(lambda _, r=row_index: self.book_ticket(r))
                self.ui.tableWidget.setCellWidget(row_index, 8, pbtn)

    def calculate_duration(self, departure, arrival):
        """计算耗费的时间"""
        departure_time = datetime.strptime(departure, '%H:%M')
        arrival_time = datetime.strptime(arrival, '%H:%M')
        return (arrival_time - departure_time).seconds / 60

    # 函数：计算中转航班总价格
    def calculate_total_price(self, flight_info):
        """计算总价格"""
        return int(flight_info[7]) + int(flight_info[-1])

    """归并排序算法"""

    # 价格排序
    def merge_sort_price(self, flights):
        if len(flights) > 1:
            mid = len(flights) // 2
            left_half = self.merge_sort_price(flights[:mid])
            right_half = self.merge_sort_price(flights[mid:])

            return self.merge_price(left_half, right_half)
        return flights

    def merge_price(self, left, right):
        sorted_list = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if self.is_direct_flight(left[left_index]):
                left_price = int(left[left_index][-1])
            else:
                left_price = self.calculate_total_price(left[left_index])

            if self.is_direct_flight(right[right_index]):
                right_price = int(right[right_index][-1])
            else:
                right_price = self.calculate_total_price(right[right_index])

            if left_price < right_price:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1

        sorted_list.extend(left[left_index:])
        sorted_list.extend(right[right_index:])

        return sorted_list

    # 时间排序
    def merge_sort_time(self, flights):
        if len(flights) > 1:
            mid = len(flights) // 2
            left_half = self.merge_sort_time(flights[:mid])
            right_half = self.merge_sort_time(flights[mid:])

            return self.merge_time(left_half, right_half)
        return flights

    def merge_time(self, left, right):
        sorted_list = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if self.is_direct_flight(left[left_index]):
                left_time = self.calculate_duration(left[left_index][4], left[left_index][5])
            else:
                left_time = self.calculate_duration(left[left_index][4], left[left_index][-3])

            if self.is_direct_flight(right[right_index]):
                right_time = self.calculate_duration(right[right_index][4], right[right_index][5])
            else:
                right_time = self.calculate_duration(right[right_index][4], right[right_index][-3])

            if left_time < right_time:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1
        sorted_list.extend(left[left_index:])
        sorted_list.extend(right[right_index:])
        return sorted_list

    # 判断是否为直达航班
    def is_direct_flight(self, flight):
        return len(flight) == 8

    def z_time_sort(self):
        """时间排序"""
        if not len(self.all_flights):
            QMessageBox.information(self, '提示', '当前列表中没有航班信息')
            return
        else:
            sorted_flights = self.merge_sort_time(self.all_flights)
            results = []
            for flight in sorted_flights:
                if self.is_direct_flight(flight):
                    results.append(flight)
                else:
                    results.append(flight[:8])
                    results.append(flight[8:])
            for row_index, row_data in enumerate(results):
                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.ui.tableWidget.setItem(row_index, col_index, item)
                    pbtn = QPushButton("订票")
                    # 这里不可以直接写成self.book_ticket(row_index)
                    pbtn.clicked.connect(lambda _, r=row_index: self.book_ticket(r))
                    self.ui.tableWidget.setCellWidget(row_index, 8, pbtn)

    def z_price_sort(self):
        """价格排序"""
        if not len(self.all_flights):
            QMessageBox.information(self, '提示', '当前列表中没有航班信息')
            return
        else:
            sorted_flights = self.merge_sort_price(self.all_flights)
            results = []
            for flight in sorted_flights:
                if self.is_direct_flight(flight):
                    results.append(flight)
                else:
                    results.append(flight[:8])
                    results.append(flight[8:])

            for row_index, row_data in enumerate(results):
                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.ui.tableWidget.setItem(row_index, col_index, item)
                    pbtn = QPushButton("订票")
                    # 这里不可以直接写成self.book_ticket(row_index)
                    pbtn.clicked.connect(lambda _, r=row_index: self.book_ticket(r))
                    self.ui.tableWidget.setCellWidget(row_index, 8, pbtn)

    def homeshai(self):
        """筛选"""
        choose = self.ui.comboBox.currentText()
        text = self.ui.lineEdit.text()
        chu = self.ui.lineEditChu.text()
        dao = self.ui.lineEditDao.text()
        date = self.ui.comboBox_2.currentText()
        if not text:
            self.ui.stackedWidget_3.setCurrentIndex(2)
            return
        if chu and dao and date:
            zhida = sql.search_flights_in_file(chu, dao, date, config.file_path_flights)
            zhongzhuan = sql.find_one_stop_connections(chu, dao, date, config.file_path_flights)
            self.all_flights[:] = zhida + zhongzhuan
            # print(self.all_flights)
            filtered_flights = sql.filter_flights_in_list(choose, text, chu, dao, date, self.all_flights)
            # print(filtered_flights)
            results = []
            for line in filtered_flights:
                if len(line) > 8:
                    results.append(line[:8])
                    results.append(line[8:])
                else:
                    results.append(line)
        else:
            results = sql.filter_flights_in_file(choose, text, chu, dao, date, config.file_path_flights)
        self.all_flights[:] = results
        if not len(results):
            self.ui.stackedWidget_3.setCurrentIndex(1)
        else:
            self.ui.stackedWidget_3.setCurrentIndex(3)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(results))
        for row_index, row_data in enumerate(results):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row_index, col_index, item)
                pbtn = QPushButton("订票")
                # 这里不可以直接写成self.book_ticket(row_index)
                pbtn.clicked.connect(lambda _, r=row_index: self.book_ticket(r))
                self.ui.tableWidget.setCellWidget(row_index, 8, pbtn)

    def book_ticket(self, row):
        """订票"""
        self.ui.stackedWidget_5.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(3)
        flight_number = self.ui.tableWidget.item(row, 0).text()
        departure = self.ui.tableWidget.item(row, 1).text()
        arrival = self.ui.tableWidget.item(row, 2).text()
        schedule = self.ui.tableWidget.item(row, 3).text()
        departure_time = self.ui.tableWidget.item(row, 4).text()
        arrival_time = self.ui.tableWidget.item(row, 5).text()
        price = self.ui.tableWidget.item(row, 7).text()
        if schedule == '每日':
            schedule = '1.2.3.4.5.6.7'
        self.ui.comboBox_date.clear()
        self.ui.comboBox_date.addItems(schedule.split('.'))
        self.ui.lineEditCode.setText(flight_number)
        self.ui.lineEditCode.setReadOnly(True)
        self.ui.lineEditLauTime.setText(departure_time)
        self.ui.lineEditLauTime.setReadOnly(True)
        self.ui.lineEditArrTime.setText(arrival_time)
        self.ui.lineEditArrTime.setReadOnly(True)
        self.ui.lineEditArr.setText(arrival)
        self.ui.lineEditArr.setReadOnly(True)
        self.ui.lineEditLau.setText(departure)
        self.ui.lineEditLau.setReadOnly(True)
        self.ui.lineEditPrice1.setText(price)
        self.ui.lineEditPrice1.setReadOnly(True)

    def book_confirm(self):
        date = self.ui.comboBox_date.currentText()
        flight_number = self.ui.lineEditCode.text()
        chu_t = self.ui.lineEditLauTime.text()
        dao_t = self.ui.lineEditArrTime.text()
        dao = self.ui.lineEditArr.text()
        chu = self.ui.lineEditLau.text()
        price = self.ui.lineEditPrice1.text()
        new_flight_info = f"\n{config.user_now},{flight_number},{chu},{dao},{date},{chu_t},{dao_t},{price}"
        # 检查票数是否不足
        result = sql.ticket_sub1(flight_number, config.file_path_flights)
        if not result:
            QMessageBox.information(self, '错误', '票数不足，请选择其他航班')
        else:
            sql.add_tickets(new_flight_info, config.file_path_tickets)
            self.ui.stackedWidget_5.setCurrentIndex(3)

    def my_tickets(self):
        results = sql.find_myticket_in_file(config.user_now, config.file_path_tickets)
        if not results:
            self.ui.stackedWidget_6.setCurrentIndex(1)
        else:
            self.ui.stackedWidget_6.setCurrentIndex(3)
        self.ui.tableWidget_3.setRowCount(0)
        self.ui.tableWidget_3.setRowCount(len(results))
        for row_index, row_data in enumerate(results):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget_3.setItem(row_index, col_index, item)
                #pbtn1 = QPushButton("改签")
                pbtn2 = QPushButton("退订")
                # 这里不可以直接写成self.book_ticket(row_index)
                #pbtn1.clicked.connect(lambda _, r=row_index: self.edit_ticket(r))
                #self.ui.tableWidget_3.setCellWidget(row_index, 7, pbtn1)
                pbtn2.clicked.connect(lambda _, r=row_index: self.delete_ticket(r))
                self.ui.tableWidget_3.setCellWidget(row_index, 7, pbtn2)

    #def edit_ticket(self, row):
    #    self.ui.stackedWidget.setCurrentIndex(4)
    #    pass

    def delete_ticket(self, row):
        """删除航班信息"""
        flight_number = self.ui.tableWidget_3.item(row, 0).text()
        date = self.ui.tableWidget_3.item(row, 3).text()
        result = sql.delete_ticket(config.user_now, flight_number, date, config.file_path_tickets)
        if result:
            QMessageBox.information(self, '成功', '退订成功')
            sql.ticket_add1(flight_number, config.file_path_flights)
            # 刷新表格或执行其他必要的清理工作
            self.my_tickets()  # 刷新表格的函数


"""用于调试用"""
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = UserWindow()
    sys.exit(app.exec_())
