#!/usr/bin/env python3
"""Module for task 0"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int: int]:
    """The funciton returns a tuple of size two containing a start
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
