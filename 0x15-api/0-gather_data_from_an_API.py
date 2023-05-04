#!/usr/bin/python3
"""Use API for a given user id and return information containing
   the person's TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    req = requests.get(f'https://jsonplaceholder.typicode.com/users?id={id}')
    name = req.json()[0]['name']
    reqt = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    total = len(reqt.json())
    count = 0
    tasks = []
    for i in reqt.json():
        for k in i.keys():
            if k == 'completed':
                if i[k] is True:
                    count = count + 1
                    tasks.append(i)
    print(f'Eployee {name} is done with tasks ({count}/{total}):')
    for i in tasks:
        for k in i.keys():
            if k == 'title':
                print(f'\t {i[k]}')
