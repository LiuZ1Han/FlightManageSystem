# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(993, 372)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 40, 171, 271))
        self.frame.setStyleSheet("#frame{\n"
"image: url(:/imag/imag/login1.png);\n"
"image-border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 80, 126, 23))
        self.label.setStyleSheet("\n"
"font: 16pt \"华文行楷\";\n"
"color: rgb(133, 151, 251);")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(240, 50, 301, 251))
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.0113636, y2:0, stop:0 rgba(255, 241, 211, 255), stop:1 rgba(255, 236, 227, 255));\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 17, 301, 234))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(301, 234))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(18)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget_2.setStyleSheet("QLineEdit{\n"
"    border:none;\n"
"    border-bottom:1px solid black;\n"
"}\n"
"QPushButton{\n"
"    border-radius:7px;\n"
"    background-color: rgb(255, 230, 198);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:3px;\n"
"    padding-left:3px;\n"
"}")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.pushButton_L_confirm = QtWidgets.QPushButton(self.page_login)
        self.pushButton_L_confirm.setGeometry(QtCore.QRect(60, 140, 161, 23))
        self.pushButton_L_confirm.setObjectName("pushButton_L_confirm")
        self.radioButton_user = QtWidgets.QRadioButton(self.page_login)
        self.radioButton_user.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.radioButton_user.setObjectName("radioButton_user")
        self.radioButton_manageruser = QtWidgets.QRadioButton(self.page_login)
        self.radioButton_manageruser.setGeometry(QtCore.QRect(90, 100, 86, 16))
        self.radioButton_manageruser.setObjectName("radioButton_manageruser")
        self.radioButton_supermanager = QtWidgets.QRadioButton(self.page_login)
        self.radioButton_supermanager.setGeometry(QtCore.QRect(190, 100, 86, 16))
        self.radioButton_supermanager.setObjectName("radioButton_supermanager")
        self.lineEdit_L_password = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_L_password.setGeometry(QtCore.QRect(60, 60, 161, 20))
        self.lineEdit_L_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_L_password.setObjectName("lineEdit_L_password")
        self.lineEdit_L_account = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_L_account.setGeometry(QtCore.QRect(60, 20, 161, 20))
        self.lineEdit_L_account.setObjectName("lineEdit_L_account")
        self.stackedWidget_2.addWidget(self.page_login)
        self.page_register = QtWidgets.QWidget()
        self.page_register.setObjectName("page_register")
        self.lineEdit_R_account = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_R_account.setGeometry(QtCore.QRect(70, 20, 151, 17))
        self.lineEdit_R_account.setObjectName("lineEdit_R_account")
        self.lineEdit_R_password = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_R_password.setGeometry(QtCore.QRect(70, 60, 151, 17))
        self.lineEdit_R_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_R_password.setObjectName("lineEdit_R_password")
        self.lineEdit_R_repassword = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_R_repassword.setGeometry(QtCore.QRect(70, 100, 151, 17))
        self.lineEdit_R_repassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_R_repassword.setObjectName("lineEdit_R_repassword")
        self.pushButton_R_confirm = QtWidgets.QPushButton(self.page_register)
        self.pushButton_R_confirm.setGeometry(QtCore.QRect(60, 140, 161, 21))
        self.pushButton_R_confirm.setObjectName("pushButton_R_confirm")
        self.stackedWidget_2.addWidget(self.page_register)
        self.verticalLayout_4.addWidget(self.stackedWidget_2)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Login = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Login.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:3px;\n"
"    padding-left:3px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imag/imag/login_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Login.setIcon(icon)
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.horizontalLayout.addWidget(self.pushButton_Login)
        self.pushButton_Register = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Register.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    padding-bottom:3px;\n"
"    padding-left:3px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imag/imag/login_icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Register.setIcon(icon1)
        self.pushButton_Register.setObjectName("pushButton_Register")
        self.horizontalLayout.addWidget(self.pushButton_Register)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(93, 9, 99, 12))
        self.label_3.setStyleSheet("color:rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setGeometry(QtCore.QRect(110, 7, 71, 14))
        self.label_4.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.page_5)
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.page_6)
        self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.page_7)
        self.label_7.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_5)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(280, 0, 20, 20))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:3px;\n"
"}")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imag/imag/exit.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(16, 20))
        self.pushButton.setObjectName("pushButton")
        self.frame_2.raise_()
        self.frame.raise_()
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(LoginWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "环球航空公司"))
        self.pushButton_L_confirm.setText(_translate("LoginWindow", "确认"))
        self.radioButton_user.setText(_translate("LoginWindow", "普通用户"))
        self.radioButton_manageruser.setText(_translate("LoginWindow", "航班管理用户"))
        self.radioButton_supermanager.setText(_translate("LoginWindow", "超级管理员"))
        self.lineEdit_L_password.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.lineEdit_L_account.setPlaceholderText(_translate("LoginWindow", "账号："))
        self.lineEdit_R_account.setPlaceholderText(_translate("LoginWindow", "账号："))
        self.lineEdit_R_password.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.lineEdit_R_repassword.setPlaceholderText(_translate("LoginWindow", "确认密码："))
        self.pushButton_R_confirm.setText(_translate("LoginWindow", "注册"))
        self.pushButton_Login.setText(_translate("LoginWindow", "登录"))
        self.pushButton_Register.setText(_translate("LoginWindow", "注册"))
        self.label_2.setText(_translate("LoginWindow", "             账号或密码不能为空！"))
        self.label_3.setText(_translate("LoginWindow", "账号或密码错误！"))
        self.label_4.setText(_translate("LoginWindow", "未选择角色！"))
        self.label_5.setText(_translate("LoginWindow", "               两次密码不一致！"))
        self.label_6.setText(_translate("LoginWindow", "该账号已存在，请重新输入账号！"))
        self.label_7.setText(_translate("LoginWindow", "注册成功！"))
import res_rc
