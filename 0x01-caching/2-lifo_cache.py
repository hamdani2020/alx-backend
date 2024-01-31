#!/usr/bin/env python3
"""Module for Last-In First-Out
"""
from base_caching import BaseCaching

from collections import OrderedDict


class LIFOCache(BaseCaching):
    """It represents an object that allows the storing
     and getting of items using LIFO."""

    def __init__(self):
        """ Initializes
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """It adds items in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ It gets an item by key
        """
        return self.cache_data.get(key, None)
