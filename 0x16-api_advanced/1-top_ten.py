#!/usr/bin/python3
"""Query Reddit API and print the titles of the first
   10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Query number of subcsribers of subreddit
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' +
               'AppleWebKit/537.36 (KHTML, like Gecko)' +
               'Chrome/58.0.3029.110 Safari/537.3'}
    resp = requests.get('https://www.reddit.com/r/{}/hot/.json'.
                        format(subreddit), allow_redirects=False,
                        headers=headers)
    if resp.status_code == '429':
        pass
    else:
        json = resp.json()
        if json.get('data'):
            titles = [t['data']['title'] for t in json.get('data').get
                      ('children')]
            top_ten = titles[:10]
            for title in top_ten:
                print(title)
        else:
            print('None')
