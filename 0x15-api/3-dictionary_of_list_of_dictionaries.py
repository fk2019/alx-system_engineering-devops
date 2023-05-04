#!/usr/bin/python3
"""Use API for all users' ids and export all information of
   to a JSON file
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user_info = {}
    for user in users:
        id = user.get('id')
        username = user.get('username')
        todos_list = [i for i in todos if i.get('userId') == id]
        user_l = []
        for i in todos_list:
            user_l.append({'username': username, 'task': i.get('title'),
                           'completed': i.get('completed')})
        user_info['{}'.format(id)] = user_l
    with open('todo_all_employees.json', 'w', encoding='utf8') as f:
        json.dump(user_info, f)
