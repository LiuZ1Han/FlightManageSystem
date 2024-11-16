"""
登录GUI以及相关操作
"""
from UI.LoginUI import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import config
import sql


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user_win = None
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        # 隐藏外部窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 阴影
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(1, 1)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QtCore.Qt.gray)
        self.ui.frame.setGraphicsEffect(self.shadow)
        # 登录与注册页面的跳转
        self.ui.pushButton_Login.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_Register.clicked.connect(self.status_user)
        # 登录确认
        self.ui.pushButton_L_confirm.clicked.connect(self.login_in)
        # 注册确认
        self.ui.pushButton_R_confirm.clicked.connect(self.register_in)
        # 页面显示
        self.show()

    """获取用户状态"""

    def status_user(self):
        if not (self.ui.radioButton_user.isChecked()
                or self.ui.radioButton_manageruser.isChecked()
                or self.ui.radioButton_supermanager.isChecked()):
            self.ui.stackedWidget.setCurrentIndex(3)
        else:
            self.ui.stackedWidget_2.setCurrentIndex(1)

    """登入函数"""

    def login_in(self):
        account = self.ui.lineEdit_L_account.text()
        password = self.ui.lineEdit_L_password.text()
        if self.ui.radioButton_user.isChecked():
            # 从文本文件中读取用户数据
            users_data = sql.read_users_from_file(config.file_path_users)

            # 检查账号密码是否正确
            if len(account) == 0 or len(password) == 0:
                self.ui.stackedWidget.setCurrentIndex(1)
            elif account in users_data and users_data[account] == password:
                config.user_now = account
                from ClassUI.classuser import UserWindow
                self.user_win = UserWindow()
                self.close()
            else:
                self.ui.stackedWidget.setCurrentIndex(2)
        elif self.ui.radioButton_manageruser.isChecked():
            users_data = sql.read_users_from_file(config.file_path_managers)
            if len(account) == 0 or len(password) == 0:
                self.ui.stackedWidget.setCurrentIndex(1)
            elif account in users_data and users_data[account] == password:
                config.user_now = account
                from ClassUI.classmanageruser import ManageruserWindow
                self.user_win = ManageruserWindow()
                self.close()
            else:
                self.ui.stackedWidget.setCurrentIndex(2)
        elif self.ui.radioButton_supermanager.isChecked():
            users_data = sql.read_users_from_file(config.file_path_supers)
            if len(account) == 0 or len(password) == 0:
                self.ui.stackedWidget.setCurrentIndex(1)
            elif account in users_data and users_data[account] == password:
                config.user_now = account
                from ClassUI.classsuper import SuperWindow
                self.user_win = SuperWindow()
                self.close()
            else:
                self.ui.stackedWidget.setCurrentIndex(2)
        else:
            self.ui.stackedWidget.setCurrentIndex(3)  # 没有选中任何 RadioButton，显示错误界面
        return

    """注册账号，关联到不同的角色"""

    def register_in(self):
        account = self.ui.lineEdit_R_account.text()
        pass_1 = self.ui.lineEdit_R_password.text()
        pass_2 = self.ui.lineEdit_R_repassword.text()
        if self.ui.radioButton_user.isChecked():
            dict_user = sql.read_users_from_file(config.file_path_users)
            if len(account) == 0 or len(pass_1) == 0 or len(pass_2) == 0:
                self.ui.stackedWidget.setCurrentIndex(1)
            elif account in dict_user:
                self.ui.stackedWidget.setCurrentIndex(5)
            elif pass_1 != pass_2:
                self.ui.stackedWidget.setCurrentIndex(4)
            else:
                sql.write_user_to_file(account, pass_1, config.file_path_users)
                self.ui.stackedWidget.setCurrentIndex(6)

        elif self.ui.radioButton_manageruser.isChecked():
            dict_user = sql.read_users_from_file(config.file_path_managers)
            if len(account) == 0 or len(pass_1) == 0 or len(pass_2) == 0:
                self.ui.stackedWidget.setCurrentIndex(1)
            elif account in dict_user:
                self.ui.stackedWidget.setCurrentIndex(5)
            elif pass_1 != pass_2:
                self.ui.stackedWidget.setCurrentIndex(4)
            else:
                sql.write_user_to_file(account, pass_1, config.file_path_managers)
                self.ui.stackedWidget.setCurrentIndex(6)

        elif self.ui.radioButton_supermanager.isChecked():
            dict_user = sql.read_users_from_file(config.file_path_supers)
            if len(account) == 0 or len(pass_1) == 0 or len(pass_2) == 0:
                self.ui.stackedWidget.setCurrentIndex(1)
            elif account in dict_user:
                self.ui.stackedWidget.setCurrentIndex(5)
            elif pass_1 != pass_2:
                self.ui.stackedWidget.setCurrentIndex(4)
            else:
                sql.write_user_to_file(account, pass_1, config.file_path_supers)
                self.ui.stackedWidget.setCurrentIndex(6)
        return


"""用于调试用"""
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
