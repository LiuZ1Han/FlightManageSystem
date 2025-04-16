## FlightManageSystem
航班订票管理系统  
其中的res.qrc需要使用PyCharm中的外部工具PyRIC，将其转换成py文件。  
## 文件结构
```bash
E:
│  main.py  // 主函数
|  config.py
|  sql.py
│  
├─data
│  │  fights.txt
│  │  managers.txt
|  |  super.txt
|  |  tickets.txt
|  |  users.txt
│
│                  
├─ClassUI
│  |  classlogin.py
|  |  classmanageruser.py
│  |  classsuper.py
│  |  classuser.py
|
|
|─UI
|  │  LoginUI.py  // 登录页面Ui的py版本
|  │  LoginUI.ui  // 登录页面Ui的源程序
|  |  ManageruserUI.py  // 普通管理员页面Ui的py版本
|  │  ManageruserUI.ui  // 普通管理员页面Ui的源程序
|  |  SupermanagerUI.py  // 超级管理员页面Ui的py版本
|  │  SupermanagerUI.ui  // 超级管理员页面Ui的源程序
|  │  UserUI.py  // 用户页面Ui的py版本
|  │  UserUI.ui  // 用户页面Ui的源程序
|
|-image // 存放GUI界面涉及到的所有图标
```
## 功能框架图
# 普通用户功能框架
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/Figure1.jpg)
# 航班管理员用户功能框架
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/Figure2.jpg)
# 超级管理员用户功能框架
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/Figure3.jpg)
## 运行结果图
# 普通用户端
登录界面
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/Figure4.jpg)
用户查询界面
可以查找中转航班信息
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/Figure5.jpg)
订票界面
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/F6.jpg)
查询个人机票
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/F7.jpg)
修改密码
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/F8.jpg)
## 管理员用户界面
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/F9.jpg)
## 超级管理员用户界面
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/F10.jpg)

