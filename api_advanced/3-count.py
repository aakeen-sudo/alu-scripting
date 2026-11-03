#!/usr/bin/python3
"""Recursively count keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the given keywords in hot post titles."""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data")
    words = [word.lower() for word in word_list]

    for post in data.get("children"):
        title = post.get("data").get("title").lower().split()
        for word in set(words):
            found = title.count(word) * words.count(word)
            counts[word] = counts.get(word, 0) + found

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    results = [(word, count) for word, count in counts.items() if count > 0]
    results.sort(key=lambda item: (-item[1], item[0]))
    for word, count in results:
        print("{}: {}".format(word, count))
