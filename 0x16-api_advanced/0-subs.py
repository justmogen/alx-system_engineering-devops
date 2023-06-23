#!/usr/bin/python3
"""This function will query number of subscribers on specified subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns total subscribers on the given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
