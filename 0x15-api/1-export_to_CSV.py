#!/usr/bin/python3
"""Use API for a given user id and export information of
   the person's TODO list progress in a csv file
"""
import csv
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    req = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.
                       format(id))
    name = req.json()[0].get('username')
    reqt = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))
    tasks = reqt.json()
    data = []
    for i in tasks:
        data.append({'name': name, 'id': id, 'completed': i['completed'],
                     'title': i['title']})
    with open('USER_ID.csv', 'w', newline='') as csvfile:
        fn = ['id', 'name', 'completed', 'title']
        writer = csv.DictWriter(csvfile, fieldnames=fn, quoting=csv.QUOTE_ALL)
        for d in data:
            writer.writerow(d)
