#!/usr/bin/python3
"""Use API for a given user id and return information containing
   the person's TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    req = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.
                       format(id))
    name = req.json()[0].get('name')
    reqt = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))
    total = len(reqt.json())
    count = 0
    tasks = []
    for i in reqt.json():
        if i.get('completed') is True:
            count = count + 1
            tasks.append(i)
    print('Employee {} is done with tasks({}/{}):'.format(name, count, total))
    for i in tasks:
        if i.get('title'):
            print('\t {}'.format(i.get("title")))
