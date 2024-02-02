#!/usr/bin/python3
"""
Module Least Frequently Used (LFU)
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    It creates the LFUCache system without limit
    """
    def __init__(self):
        """
        Initiation
        """
        super().__init__()
        self.uses = dict()

    def put(self, key, item):
        """
        It adds an item in the cache
        """
        if key is None or item is None:
            return
        if (len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
            and key not in self.cache_data.keys()):
            discardKey = min(self.uses, key=self.uses.get)
            del self.cache_data[discardKey]
            del self.uses[discardKey]
            print("DISCARD: {}".format(discardKey))
        if key in self.cache_data.keys():
            self.uses[key] += 1
        else:
            self.uses[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """
        it retrieves an item by key
        """
        if key is None or key not in self.cache_data.keys():
            return
        self.uses[key] += 1
        return self.cache_data.get(key)
