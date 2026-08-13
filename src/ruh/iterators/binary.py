from ruh.iterators.base import BaseIterator
from typing import TypeVar

T = TypeVar("T")


class _BinarySplitIterator(BaseIterator):

    def remaining(self):
        return self._end - self._index

    def split(self):
        m = (self._start + self._end) // 2
        l = _BinarySplitIterator(self._items, start=self._start, end=m)
        r = _BinarySplitIterator(self._items, start=m, end=self._end)
        return l, r


class BinarySplitIterator:
    def __init__(self, items: list[T]) -> None:
        self._items = items

    def __iter__(self) -> _BinarySplitIterator:
        return _BinarySplitIterator(self._items, start=0, end=len(self.items))

    @property
    def items(self) -> list[T]:
        return self._items
