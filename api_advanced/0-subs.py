#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total subscribers of a subreddit, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by aakeen-sudo)"}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return 0
        return response.json().get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
