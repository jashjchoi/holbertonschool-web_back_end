#!/usr/bin/env python3
"""Simple pagination
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        find the correct indexes to paginate the dataset correctly
        return the appropriate page of the dataset
        (i.e. the correct list of rows)
        """
        end = page * page_size
        initial = end - page_size

        return(initial, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get and return the correct page"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        data = self.dataset()
        start, end = self.index_range(page, page_size)
        if end > len(data):
            return []
        return [list(data[row]) for row in range(start, end)]
