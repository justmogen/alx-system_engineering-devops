#!/usr/bin/python3
"""
This function queries the Reddit API and returns list of titles of all hot
articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers,params=params,
                allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get("data")
        after = posts.get("after")
        count += posts.get("dist")
        for c in posts.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        else:    
            return hot_list

    else:
        return None
