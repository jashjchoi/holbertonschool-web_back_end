#!/usr/bin/env python3
"""Implement of web cache
"""

import redis
import requests
from typing import Callable
from functools import wraps

red = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """tracks number of times a particular URL
    was accessed
    """
    @wraps(method)
    def wrapper(url):
        """wrapper function"""
        red.incr(f"count:{url}")
        cached_page = red.get(f"cached:{url}")
        if cached_page:
            return cached_page.decode('utf-8')

        html_page = method(url)
        red.setex(f"cached:{url}", 10, html_page)
        return html_page
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Return html page of url
    """
    req = requests.get(url)
    return req.text
