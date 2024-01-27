#!/usr/bin/env python3
"""Module for task 0"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int: int]:
    """The funciton returns a tuple of size two containing a start
    index and and end index corresponding to the indexes to return
    in a list for those particular pagination parameters
    """
    start = (page -1) * page_size
    end = start + page_size
    return(start, end)
