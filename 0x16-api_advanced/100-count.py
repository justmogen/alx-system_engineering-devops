import requests


def get_hot_articles(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Reddit Keyword Counter"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data.get("data", {}).get("children", [])


def count_words(subreddit, word_list, index=0, counts=None):
    if counts is None:
        counts = {}

    if index < len(word_list):
        keyword = word_list[index].lower()
        hot_articles = get_hot_articles(subreddit)

        for article in hot_articles:
            title = article["data"]["title"].lower()
            counts[keyword] = counts.get(keyword, 0) + title.count(keyword)

        count_words(subreddit, word_list, index + 1, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)
