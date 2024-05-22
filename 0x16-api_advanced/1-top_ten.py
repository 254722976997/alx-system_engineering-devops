#!/usr/bin/python3
"""
Function retrieve & print the titles of top 10 hot posts in a subreddit.
"""
import requests


headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def top_ten(subreddit):
    """
    Function retrieve & print the titles of top 10 hot posts in a subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
