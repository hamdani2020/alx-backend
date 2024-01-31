#!/usr/bin/env python3
"""Module for First-In First-Out caching module
"""

from base_caching import BaseCaching

from collections import OrderedDict


class FIFOCache(BaseCaching):
    """It represents an object that allows storing
    and retrieving items using FIFO mechanism
    """
    def __init__(self):
        """ Initializes
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ It adds items in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """ It gets an item by key name
        """
        return self.cache_data.get(key, None)
