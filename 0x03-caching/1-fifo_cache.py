#!/usr/bin/python3
"""FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class
    """
    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """
        put item into cache_data with FIFO algorithm
        If key or item is None, this method should not do anything
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            delete = self.__keys.pop(0)
            del self.cache_data[delete]
            print('DISCARD: {}'.format(delete))
        if key and item:
            self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        get value of cache_data dictionary
        return the value in self.cache_data linked to key
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
