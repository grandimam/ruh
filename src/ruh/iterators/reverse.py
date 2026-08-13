from typing import TypeVar
from ruh.iterators.base import BaseIterator

T = TypeVar("T")


class _Iterator(BaseIterator):
    def __next__(self):
        if self.index <= self._end:
            raise StopIteration
        item = self._items[self.index - 1]
        self.index -= 1
        return item


class ReverseIterator:
    def __init__(self, items):
        self._items = items

    def __iter__(self):
        return _Iterator(self._items, start=len(self._items), end=0)
