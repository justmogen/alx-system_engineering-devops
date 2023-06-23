#!/usr/bin/python3
"""This function queries for top 10  hot posts for a give subreddit."""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for i in range(10):
            title = posts[i]["data"]["title"]
            print(title)
    else:
        print(None)
