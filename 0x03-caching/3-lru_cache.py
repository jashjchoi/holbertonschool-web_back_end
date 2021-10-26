#!/usr/bin/env python3
"""LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    Caching system and Inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """
        put item into cache_data with LIFO algorithm
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.__keys:
                self.__keys.append(key)
            else:
                self.__keys.append(self.__keys.pop(
                    self.__keys.index(key)))
            if len(self.__keys) > BaseCaching.MAX_ITEMS:
                delete = self.__keys.pop(0)
                del self.cache_data[delete]
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """"
        get value of cache_data dictionary
        return the value in self.cache_data linked to key
        """
        if key and key in self.cache_data:
            self.__keys.append(self.__keys.pop(
                self.current_keys.index(key)))
            return self.cache_data.get(key)
        return None
