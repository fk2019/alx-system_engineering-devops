#!/usr/bin/python3
"""Use API for a given user id and return information containing
   the person's TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    req = requests.get(f'https://jsonplaceholder.typicode.com/users?id={id}')
    name = req.json()[0].get('name')
    reqt = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    total = len(reqt.json())
    count = 0
    tasks = []
    for i in reqt.json():
        if i.get('completed') is True:
            count = count + 1
            tasks.append(i)
    print(f'Employee {name} is done with tasks ({count}/{total}):')
    for i in tasks:
        if i.get('title'):
            print(f'\t {i.get("title")}')
