#!/usr/bin/env python3
"""Module for Least Recently Used (LRU)
"""
from base_caching import BaseCaching

from collections import OrderedDict


class LRUCache(BaseCaching):
    """It represents an object that allows the storing
    and getting items using LRU
    """
    def __init__(self):
        """Initializes
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ It puts an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """It gets an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
