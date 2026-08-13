from typing import TypeVar

T = TypeVar('T')

class _Iterator:

    def __init__(self, items: list[T], max_size: int) -> None:
        self._items = items
        self._max_size = max_size
        self._index = 0

    def __next__(self) -> T:
        if self._index >= len(self._items):
            raise StopIteration
        item = self._items[self._index]
        self._index += 1
        return item

    def __iter__(self) -> "_Iterator":
        return self

    def split(self) -> tuple["_Iterator", "_Iterator"]:
        if len(self._items) <= self._max_size:
            raise StopIteration
        m = min(self._max_size, len(self._items))
        l = _Iterator(self._items[0: m], self._max_size)
        r = _Iterator(self._items[m:], self._max_size)
        return l, r


class FixedSizedSplitIterator:

    def __init__(self, items: list[T], max_size: int):
        self._items = items
        self._max_size = max_size

    @property
    def items(self) -> list[T]:
        return self._items

    @property
    def max_size(self) -> int:
        return self._max_size

    def __iter__(self):
        return _Iterator(self.items, self.max_size)
