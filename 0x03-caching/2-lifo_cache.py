#!/usr/bin/python3
"""LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Caching system and Inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """put item into cache_data with LIFO algorithm"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.__keys))
                self.cache_data.pop(self.__keys)
            self.__keys = key

    def get(self, key):
        """
        get value of cache_data dictionary
        return the value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
