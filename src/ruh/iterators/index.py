from ruh.iterators.base import BaseIterator
from typing import TypeVar

T = TypeVar("T")


class _Iterator(BaseIterator):
    pass


class IndexIterator:
    def __init__(self, items: list[T]):
        if not items:
            raise TypeError("IndexIterator must have at least one item")
        self._items = items

    def __iter__(self):
        return _Iterator(self._items, start=0, end=len(self._items))
