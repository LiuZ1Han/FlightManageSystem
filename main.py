"""
运行该文件即可
"""
if __name__ == '__main__':
    from UI.LoginUI import *
    from PyQt5.QtWidgets import QApplication
    import sys
    from ClassUI.classlogin import LoginWindow
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())