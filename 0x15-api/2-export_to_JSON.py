#!/usr/bin/python3
"""Use API for a given user id and export information of
   the person's TODO list progress in a JSON file
"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    req = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.
                       format(id))
    username = req.json()[0].get('username')
    reqt = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))
    tasks = reqt.json()
    data = {str(id): []}
    for i in tasks:
        data[str(id)].append({'task': i['title'], 'completed': i['completed'],
                              'username': username})
    with open('USER_ID.json', 'w', encoding='utf8') as f:
        json.dump(data, f)
