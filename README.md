# FlightManageSystem
航班订票管理系统  
其中的res.qrc需要使用PyCharm中的外部工具PyRIC，将其转换成py文件。  
# 文件结构
```bash
E:
│  main.py  // 主函数
|  config.py
|  sql.py  // 所有查询、排序等操作函数实现
│  
├─data
│  │  fights.txt // 航班信息
│  │  managers.txt // 管理员信息
|  |  super.txt // 超级管理员信息
|  |  tickets.txt // 机票信息
|  |  users.txt // 用户信息
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
# 功能框架图
## 普通用户功能框架
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/Figure1.jpg)
## 航班管理员用户功能框架
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/Figure2.jpg)
## 超级管理员用户功能框架
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/Figure3.jpg)

# 运行结果图
## 普通用户端
### 登录界面
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/Figure4.png)
### 用户查询界面
可以查找中转航班信息
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/Figure5.png)
### 订票界面
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/F6.png)
### 查询个人机票
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/F7.png)
### 修改密码
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/F8.png)

## 管理员用户界面
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/F9.png)

## 超级管理员用户界面
![image](https://github.com/LiuZ1Han/FlightManageSystem/blob/main/Png/F10.png)

