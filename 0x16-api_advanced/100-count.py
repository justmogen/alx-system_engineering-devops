import requests
"""Function to count words in all hot posts of a given Reddit subreddit."""


def count_words(subreddit, word_list, instances={}, after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Custom User Agent"
    }
    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print(None)
        return

    data = response.json()
    print(data)  # Print the API response for debugging

    if "data" not in data or "children" not in data["data"]:
        print("Invalid API response")
        return

    posts = data["data"]["children"]

    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            instances[word] = instances.get(word, 0) + title.count(word)

    next_page = data["data"]["after"]
    if next_page:
        count_words(subreddit, word_list, instances, after=next_page)
    else:
        sorted_instances = sorted(instances.items(), key=lambda x: (-x[1],
                                  x[0].lower()))
        for word, count in sorted_instances:
            print(f"{word}: {count}")
