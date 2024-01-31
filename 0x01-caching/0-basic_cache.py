#!/usr/bin/env python3
"""Module for task 0
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """It allows storing and retrieving objects
    from dictionary
    """
    def put(self, key, item):
        """It adds items to the dictionary
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """It gets data by it key"""
        return self.cache_data.get(key, None)
