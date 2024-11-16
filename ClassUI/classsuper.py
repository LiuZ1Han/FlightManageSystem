"""
超级管理员GUI界面以及相关操作
"""
from UI.SupermanagerUI import *
from ClassUI.classlogin import *
from PyQt5.QtWidgets import QPushButton, QTableWidgetItem, QApplication, QMainWindow, QMessageBox
import sys
import config


class SuperWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SuperWindow()
        self.ui.setupUi(self)
        self.login_win = None
        self.original_account = None
        # 隐藏外部窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_changepass.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_muser.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButtonBack_touser.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButtonBack_tomuser.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_addu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_addm.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))

        self.ui.pushButtonBack_touser_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButtonBack_tomuser_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_5.clicked.connect(self.change_pass)
        self.ui.pushButton_Logout.clicked.connect(self.log_out)
        self.ui.pushButton_usearch.clicked.connect(self.search_users)
        self.ui.pushButton_msearch.clicked.connect(self.search_musers)
        self.ui.pushButton_2.clicked.connect(self.show_allu)
        self.ui.pushButton_6.clicked.connect(self.show_allm)
        self.ui.pushButton_8.clicked.connect(self.add_user)
        self.ui.pushButton_10.clicked.connect(self.add_muser)
        self.ui.pushButton_11.clicked.connect(self.edit_confirm)
        self.ui.pushButton_12.clicked.connect(self.edit_confirm1)

        # 页面显示
        self.show()

    def change_pass(self):
        '''修改密码'''
        new_pass1 = self.ui.lineEdit_U_pass_1.text()
        new_pass2 = self.ui.lineEdit_U_pass_2.text()
        if len(new_pass1) == 0 or len(new_pass2) == 0:
            self.ui.stackedWidget_2.setCurrentIndex(1)
        elif new_pass1 == new_pass2:
            sql.reset_password_in_file(config.user_now, new_pass1, config.file_path_supers)
            self.ui.stackedWidget_2.setCurrentIndex(3)

        else:
            self.ui.stackedWidget_2.setCurrentIndex(2)

    def log_out(self):
        config.user_now = ''
        self.close()
        from ClassUI.classlogin import LoginWindow  # 动态引入类
        self.login_win = LoginWindow()

    def search_users(self):
        """查找普通用户"""
        user = self.ui.lineEdit_uacc.text()
        if not user:
            self.ui.stackedWidget_4.setCurrentIndex(2)
            return
        results = sql.find_users_in_file(user, config.file_path_users)
        if not results:
            self.ui.stackedWidget_4.setCurrentIndex(3)
        else:
            self.ui.stackedWidget_4.setCurrentIndex(1)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(results))
        for row_index, row_data in enumerate(results):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row_index, col_index, item)
                pbtn1 = QPushButton("修改")
                pbtn3 = QPushButton("重置密码")
                pbtn2 = QPushButton("删除")
                # 这里不可以直接写成self.book_ticket(row_index)
                pbtn1.clicked.connect(lambda _, r=row_index: self.edit_user(r, 'users'))
                self.ui.tableWidget.setCellWidget(row_index, 3, pbtn1)
                pbtn2.clicked.connect(lambda _, r=row_index: self.delete_user(r, 'users'))
                self.ui.tableWidget.setCellWidget(row_index, 4, pbtn2)
                pbtn3.clicked.connect(lambda _, r=row_index: self.reset_pass(r, 'users'))
                self.ui.tableWidget.setCellWidget(row_index, 2, pbtn3)

    def search_musers(self):
        """查找航班管理用户"""
        user = self.ui.lineEdit_uacc_2.text()
        if not user:
            self.ui.stackedWidget_6.setCurrentIndex(2)
            return
        results = sql.find_users_in_file(user, config.file_path_managers)
        if not results:
            self.ui.stackedWidget_6.setCurrentIndex(3)
        else:
            self.ui.stackedWidget_6.setCurrentIndex(1)
        if not len(results):
            self.ui.stackedWidget_6.setCurrentIndex(7)
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.setRowCount(len(results))
        for row_index, row_data in enumerate(results):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget_2.setItem(row_index, col_index, item)
                pbtn1 = QPushButton("修改")
                pbtn3 = QPushButton("重置密码")
                pbtn2 = QPushButton("删除")
                # 这里不可以直接写成self.book_ticket(row_index)
                pbtn1.clicked.connect(lambda _, r=row_index: self.edit_user(r, 'managers'))
                self.ui.tableWidget_2.setCellWidget(row_index, 3, pbtn1)
                pbtn2.clicked.connect(lambda _, r=row_index: self.delete_user(r, 'managers'))
                self.ui.tableWidget_2.setCellWidget(row_index, 4, pbtn2)
                pbtn3.clicked.connect(lambda _, r=row_index: self.reset_pass(r, 'managers'))
                self.ui.tableWidget_2.setCellWidget(row_index, 2, pbtn3)

    def show_allu(self):
        """显示全部的普通用户"""
        results = sql.read_all(config.file_path_users)
        if not results:
            self.ui.stackedWidget_4.setCurrentIndex(7)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(results))
        for row_index, row_data in enumerate(results):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(row_index, col_index, item)
                pbtn1 = QPushButton("修改")
                pbtn3 = QPushButton("重置密码")
                pbtn2 = QPushButton("删除")
                # 这里不可以直接写成self.book_ticket(row_index)
                pbtn1.clicked.connect(lambda _, r=row_index: self.edit_user(r, 'users'))
                self.ui.tableWidget.setCellWidget(row_index, 3, pbtn1)
                pbtn2.clicked.connect(lambda _, r=row_index: self.delete_user(r, 'users'))
                self.ui.tableWidget.setCellWidget(row_index, 4, pbtn2)
                pbtn3.clicked.connect(lambda _, r=row_index: self.reset_pass(r, 'users'))
                self.ui.tableWidget.setCellWidget(row_index, 2, pbtn3)

    def show_allm(self):
        """显示全部的管理员用户"""
        results = sql.read_all(config.file_path_managers)
        if not len(results):
            self.ui.stackedWidget_6.setCurrentIndex(7)
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.setRowCount(len(results))
        for row_index, row_data in enumerate(results):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget_2.setItem(row_index, col_index, item)
                pbtn1 = QPushButton("修改")
                pbtn3 = QPushButton("重置密码")
                pbtn2 = QPushButton("删除")
                # 这里不可以直接写成self.book_ticket(row_index)
                pbtn1.clicked.connect(lambda _, r=row_index: self.edit_user(r, 'managers'))
                self.ui.tableWidget_2.setCellWidget(row_index, 3, pbtn1)
                pbtn2.clicked.connect(lambda _, r=row_index: self.delete_user(r, 'managers'))
                self.ui.tableWidget_2.setCellWidget(row_index, 4, pbtn2)
                pbtn3.clicked.connect(lambda _, r=row_index: self.reset_pass(r, 'managers'))
                self.ui.tableWidget_2.setCellWidget(row_index, 2, pbtn3)

    def edit_user(self, row, table_name):
        """修改用户信息"""
        if table_name == 'users':
            self.ui.stackedWidget.setCurrentIndex(5)
            self.original_account = self.ui.tableWidget.item(row, 0).text()
            password = self.ui.tableWidget.item(row, 1).text()
            self.ui.lineEdit_addmacc_2.setText(self.original_account)
            self.ui.lineEdit_addmpass_2.setText(password)

        elif table_name == 'managers':
            self.ui.stackedWidget.setCurrentIndex(6)
            self.original_account = self.ui.tableWidget_2.item(row, 0).text()
            password = self.ui.tableWidget_2.item(row, 1).text()
            self.ui.lineEdit_addmacc_3.setText(self.original_account)
            self.ui.lineEdit_addmpass_3.setText(password)

    def edit_confirm(self):
        account = self.ui.lineEdit_addmacc_2.text()
        password = self.ui.lineEdit_addmpass_2.text()
        flag = sql.check_exists(account, config.file_path_users)
        if not account or not password:
            self.ui.stackedWidget_7.setCurrentIndex(2)
        elif self.original_account != account and flag:
            self.ui.stackedWidget_7.setCurrentIndex(1)
        else:
            sql.edit_user_in_file(account, password, self.original_account, config.file_path_users)
            # 该用户的购票信息也要更新
            sql.update_ticket_account(account, self.original_account, config.file_path_tickets)
            self.ui.stackedWidget_7.setCurrentIndex(3)

    def edit_confirm1(self):
        account = self.ui.lineEdit_addmacc_3.text()
        password = self.ui.lineEdit_addmpass_3.text()
        flag = sql.check_exists(account, config.file_path_managers)
        if not account or not password:
            self.ui.stackedWidget_8.setCurrentIndex(2)
        elif self.original_account != account and flag:
            self.ui.stackedWidget_8.setCurrentIndex(1)
        else:
            sql.edit_user_in_file(account, password, self.original_account, config.file_path_managers)
            self.ui.stackedWidget_8.setCurrentIndex(3)

    def delete_user(self, row, table_name):
        if table_name == 'users':
            account = self.ui.tableWidget.item(row, 0).text()
            result = sql.delete_from_file(account, config.file_path_users)
            # 该用户的所有机票也要删除,相应航班的票数需要加1
            result_2 = sql.delete_user_update_flights(account, config.file_path_tickets, config.file_path_flights)
            if result and result_2:
                QMessageBox.information(self, '成功', '删除成功')
                self.show_allu()
            return
        elif table_name == 'managers':
            account = self.ui.tableWidget_2.item(row, 0).text()
            result = sql.delete_from_file(account, config.file_path_managers)
            if result:
                QMessageBox.information(self, '成功', '删除成功')
                self.show_allm()

    def add_muser(self):
        account = self.ui.lineEdit_addmacc.text()
        password = self.ui.lineEdit_addmpass.text()
        flag = sql.check_exists(account, config.file_path_managers)
        if not account or not password:
            self.ui.stackedWidget_5.setCurrentIndex(2)
        elif flag:
            self.ui.stackedWidget_5.setCurrentIndex(1)
        else:
            sql.write_user_to_file(account, password, config.file_path_managers)
            self.ui.stackedWidget_5.setCurrentIndex(3)

    def add_user(self):
        account = self.ui.lineEdit_adduacc.text()
        password = self.ui.lineEdit_addupass.text()
        flag = sql.check_exists(account, config.file_path_users)
        if not account or not password:
            self.ui.stackedWidget_3.setCurrentIndex(2)
        elif flag:
            self.ui.stackedWidget_3.setCurrentIndex(1)
        else:
            sql.write_user_to_file(account, password, config.file_path_users)
            self.ui.stackedWidget_3.setCurrentIndex(3)

    def reset_pass(self, row, table_name):
        """重置密码"""
        if table_name == 'users':
            account = self.ui.tableWidget.item(row, 0).text()
            password = '123456'
            result = sql.reset_password_in_file(account, password, config.file_path_users)
            if result:
                self.ui.stackedWidget_4.setCurrentIndex(6)
                self.show_allu()
            return
        elif table_name == 'managers':
            account = self.ui.tableWidget_2.item(row, 0).text()
            password = '123456'
            result = sql.reset_password_in_file(account, password, config.file_path_managers)
            if result:
                self.ui.stackedWidget_6.setCurrentIndex(6)
                self.show_allm()


"""用于调试用"""
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = SuperWindow()
    sys.exit(app.exec_())
