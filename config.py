"""
存放全局变量，文件路径
"""
import os
user_now = ''
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path_users = os.path.join(current_directory, 'data', 'users.txt')
file_path_managers = os.path.join(current_directory, 'data', 'managers.txt')
file_path_supers = os.path.join(current_directory, 'data', 'supers.txt')
file_path_flights = os.path.join(current_directory, 'data', 'flights.txt')
file_path_tickets = os.path.join(current_directory, 'data', 'tickets.txt')