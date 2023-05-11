#!/usr/bin/python3
"""Query Reddit API and return the number of subscribers
   for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Query number of subcsribers of subreddit
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' +
               'AppleWebKit/537.36 (KHTML, like Gecko)' +
               'Chrome/58.0.3029.110 Safari/537.3'}
    resp = requests.get('https://www.reddit.com/r/{}/about.json'.
                        format(subreddit), headers=headers,
                        allow_redirects=False)
    json = resp.json()
    data = json.get('data')
    return data.get('subscribers')
