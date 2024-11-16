"""
1、存放使用到的对txt操作函数
2、链表数据结构
"""
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox

"""链表数据结构"""
class Node:
    """链表的节点"""

    def __init__(self, data):
        self.data = data  # 存储信息的列表
        self.next = None  # 指向下一个节点的引用


class LinkedList:
    """链表"""
    def __init__(self):
        self.head = None  # 链表的头节点

    def append(self, data):
        """在链表末尾添加一个新的节点"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, account):
        """从链表中删除指定账号的节点"""
        current = self.head
        previous = None
        while current:
            if current.data[0] == account:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
            else:
                previous = current
            current = current.next

def read_users_from_file(file_path):
    # 读取文本文件并解析数据，不读入空行
    users_data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            strip_line = line.strip()
            if strip_line:
                user,pwd = strip_line.split(',')
                users_data[user] = pwd
    return users_data

def write_user_to_file(account, password, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:  # 'a' 模式用于追加到文件末尾
        file.write(f"\n{account},{password}")

def read_all(file_path):
    # 读取文本文件并解析数据
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip().split(',') for line in file if line.strip()]
    return lines

def check_exists(account, file_path):
    """检查用户或者航班号是否存在于文件中"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # 检查账号是否已存在
            for line in lines:
                if line:
                    existing_account = line.split(',')[0]
                    if existing_account == account:
                        return True
        return False  # 账号不存在
    except FileNotFoundError:
        return False  # 文件不存在，认为账号不存在

# 使用了链表数据结构进行删除操作
def delete_from_file(account, file_path):
    """从文件中删除指定的用户信息"""
    line_list = LinkedList()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    line_list.append(line.strip().split(','))
    except FileNotFoundError:
        return False
    # 删除账号
    line_list.delete(account)

    # 将更新后的用户信息写回文件
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            current = line_list.head
            while current:
                file.write(','.join(current.data) + '\n')
                current = current.next
    except IOError:
        return False
    return True

def reset_password_in_file(account, new_password, file_path):
    """在文件中重置指定用户密码"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        return False
    new_lines = []
    for line in lines:
        user, current_password = line.strip().split(',')
        if user == account:
            new_lines.append(f"{user},{new_password}")  # 重置密码
        else:
            new_lines.append(f"{user},{current_password}")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
    except IOError:
        return False
    return True

def binary_search(list, search_term):
    """在有序的用户列表中使用二分搜索查找包含搜索关键字的用户信息"""
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        # 检查中间元素是否包含搜索关键字
        if search_term in list[mid]:
            return list[mid]  # 找到匹配项，返回用户信息
        elif list[mid][0] < search_term:  # 假设我们按照用户名排序
            left = mid + 1
        else:
            right = mid - 1
    return None  # 没有找到匹配项

def find_users_in_file(search_term, file_path):
    """在文件中查找包含搜索关键字的用户信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip().split(',') for line in file if line.strip()]  # 读取并去除空行
            lines.sort(key=lambda x: x[0])  # 假设按照用户名排序
    except FileNotFoundError:
        return []
    # 二分法搜索用户
    return [binary_search(lines, search_term)]


def edit_user_in_file(account, new_password, original_account, file_path):
    """在文件中编辑指定用户信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        return False
    new_lines = []
    for line in lines:
        user, current_password = line.strip().split(',')
        if user == original_account:
            new_lines.append(f"{account},{new_password}")  # 更新账号和密码
        else:
            new_lines.append(f"{user},{current_password}")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
    except IOError:
        return False
    return True

def search_flights_in_file(departure, arrival, date, file_path):
    """在文件中搜索指定出发地、目的地和日期的航班信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        return []
    # 搜索航班
    found_flights = []
    for line in lines:
        flight_info = line.split(',')
        if (departure == flight_info[1] or departure == '') and \
                (arrival == flight_info[2] or arrival == '') and \
                (date in flight_info[3] or flight_info[3] == '每日' or date == ''):
            found_flights.append(flight_info)  # 添加匹配的航班信息
    return found_flights


def update_flight_in_file(original_flight_number, new_flight_info, file_path):
    """在文件中更新指定航班信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        return False
    new_lines = []
    for line in lines:
        current_flight_info = line.strip().split(',')
        if current_flight_info[0] == original_flight_number:
            new_lines.append(new_flight_info)
        else:
            new_lines.append(line)
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
    except IOError:
        return False
    return True


def add_flight_in_file(new_flight_info, file_path):
    # 添加航班
    with open(file_path, 'a', encoding='utf-8') as file:  # 'a' 模式用于追加到文件末尾
        file.write(new_flight_info)


def filter_flights_in_file(choose, text, departure, arrival, date, file_path):
    """在文件中根据给定条件筛选航班信息,对于直达的"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        return []
        # 筛选航班
    filtered_flights = []
    for line in lines:
        flight_info = line.split(',')
        # 确保所有给定的字段都符合条件
        if (choose == '航班号' and text in flight_info[0]) or \
                (choose == '最早起飞时间' and (departure == flight_info[1] or departure == '') and (
                        arrival == flight_info[2] or arrival == '')
                 and (date in flight_info[3] or flight_info[3] == '每日' or date == '')
                 and datetime.strptime(text, '%H:%M') <= datetime.strptime(flight_info[4], '%H:%M')) or \
                (choose == '最晚到达时间' and (departure == flight_info[1] or departure == '') and (
                        arrival == flight_info[2] or arrival == '')
                 and (date in flight_info[3] or flight_info[3] == '每日' or date == '')
                 and datetime.strptime(text, '%H:%M') >= datetime.strptime(flight_info[5], '%H:%M')):
            filtered_flights.append(flight_info)
    return filtered_flights


def filter_flights_in_list(choose, text, departure, arrival, date, list):
    filtered_flights = []
    for flight_info in list:
        if (choose == '航班号' and text in flight_info[0]):
            filtered_flights.append(flight_info)
        elif (choose == '最早起飞时间' and
              (departure == flight_info[1] or departure == '') and
              (arrival == flight_info[2] or arrival == '') and
              (date in flight_info[3] or flight_info[3] == '每日' or date == '') and
              datetime.strptime(text, '%H:%M') <= datetime.strptime(flight_info[4], '%H:%M')):
            filtered_flights.append(flight_info)
        elif (choose == '最晚到达时间' and
              (departure == flight_info[1] or departure == '') and
              (arrival == flight_info[2] or arrival == '') and
              (date in flight_info[3] or flight_info[3] == '每日' or date == '')
              and datetime.strptime(text, '%H:%M') >= datetime.strptime(flight_info[5], '%H:%M')):
            filtered_flights.append(flight_info)
        elif len(flight_info) > 8:
            if (choose == '最晚到达时间' and
                    departure == flight_info[1] and arrival == flight_info[10] and
                    datetime.strptime(text, '%H:%M') >= datetime.strptime(flight_info[-3], '%H:%M')):
                filtered_flights.append(flight_info)
            elif (choose == '最早起飞时间' and
                  departure == flight_info[1] and arrival == flight_info[10] and
                  datetime.strptime(text, '%H:%M') <= datetime.strptime(flight_info[4], '%H:%M')):
                filtered_flights.append(flight_info)
    return filtered_flights


def update_ticket_account(user_id, original_account, file_path):
    """用户名更新后，车票信息也要更新"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        return False
    new_lines = []
    for line in lines:
        current_flight_info = line.strip().split(',')
        if current_flight_info[0] == original_account:
            current_flight_info[0] = user_id
            new_lines.append(current_flight_info)  # 更新信息
        else:
            new_lines.append(line)  # 保留原始行
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
    except IOError:
        return False
    return True


def update_ticket_flight_number(original_flight_number, file_path):
    """航班信息更新后，若购买该航班，则机票信息删除"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        return False
    new_lines = []
    for line in lines:
        current_flight_info = line.strip().split(',')
        if not current_flight_info[1] == original_flight_number:
            new_lines.append(line)  # 保留原始行
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
    except IOError:
        return False
    return True

def add_tickets(new_ticket_info, file_path):
    # 添加订票信息
    with open(file_path, 'a', encoding='utf-8') as file:  # 'a' 模式用于追加到文件末尾
        file.write(new_ticket_info)

def ticket_sub1(flight_number, file_path):
    """更新指定航班的可订票数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        QMessageBox.information('错误', '文件不存在')
        return False
    new_lines = []
    for line in lines:
        flight_info = line.split(',')
        if flight_info[0] == flight_number:
            # 检查航班信息并更新可订票数
            available_tickets = int(flight_info[-2]) - 1  # 假设可订票数是倒数第二个字段
            if available_tickets < 0:
                return False
            flight_info[-2] = str(available_tickets)
        new_lines.append(','.join(flight_info))
    # 将更新后的内容写回文件
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
    except IOError:
        return False
    return True


def ticket_add1(flight_number, file_path):
    """更新指定航班的可订票数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        QMessageBox.information('错误', '文件不存在')
        return False
    new_lines = []
    for line in lines:
        flight_info = line.split(',')
        if flight_info[0] == flight_number:
            # 有人退票
            available_tickets = int(flight_info[-2]) + 1  # 假设可订票数是倒数第二个字段
            flight_info[-2] = str(available_tickets)
        new_lines.append(','.join(flight_info))
    # 将更新后的内容写回文件
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
    except IOError:
        return False
    return True


def delete_user_update_flights(account, file_path1, file_path2):
    """从文件中删除指定的用户信息"""
    try:
        with open(file_path1, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        return False
    # 过滤掉要删除的账号
    new_lines = []
    for line in lines:
        if line.split(',')[0] == account:
            ticket_add1(line.split(',')[1], file_path2)
        else:
            new_lines.append(line)
    # 将更新后的用户信息写回文件
    try:
        with open(file_path1, 'w', encoding='utf-8') as file:
            # 确保在写入时每行之间有换行符
            file.write('\n'.join(new_lines))
    except IOError:
        return False
    return True


def find_myticket_in_file(search_term, file_path):
    """在文件中查找包含搜索关键字的用户信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip().split(',') for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        return []
    # 搜索用户
    found_tickets = [line[1:] for line in lines if search_term in line]
    return found_tickets


def delete_ticket(account, flight_number, date, file_path):
    """从文件中删除指定的用户信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # 读取并去除空行
    except FileNotFoundError:
        return False
    # 过滤掉要删除的账号
    new_lines = []
    for line in lines:
        split_line = line.strip().split(',')
        # 只有当当前行的账户、航班号和日期不同时，才将其添加到new_lines中
        if not (split_line[0] == account and split_line[1] == flight_number and split_line[4] == date):
            new_lines.append(line)
    # 将更新后的用户信息写回文件
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            # 确保在写入时每行之间有换行符
            file.write('\n'.join(new_lines))
    except IOError:
        return False
    return True


def find_one_stop_connections(chu, dao, date, file_path):
    """找出所有只中转一次的航班方案"""
    # 搜索从出发地到任何地方的航班和从任何地方到目的地的航班
    departure_flights = search_flights_in_file(chu, '', date, file_path)
    arrival_flights = search_flights_in_file('', dao, date, file_path)

    connections = []
    # 遍历出发地航班，寻找可能的中转航班
    for flight1 in departure_flights:
        for flight2 in arrival_flights:
            # 确保航班1的目的地是航班2的出发地，并且航班1的到达时间不晚于航班2的起飞时间
            if (flight1[2] == flight2[1]
                    and datetime.strptime(flight1[5], '%H:%M') <= datetime.strptime(flight2[4], '%H:%M')):
                # 创建中转方案，组合出发航班和到达航班的信息
                connection = flight1 + flight2
                connections.append(connection)
    return connections