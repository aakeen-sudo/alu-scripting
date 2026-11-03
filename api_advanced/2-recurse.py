#!/usr/bin/python3
"""Recursively query the Reddit API for all hot post titles of a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data")
    hot_list.extend(map(lambda post: post.get("data").get("title"),
                        data.get("children")))
    after = data.get("after")
    if after is None:
        return hot_list if hot_list else None
    return recurse(subreddit, hot_list, after)
