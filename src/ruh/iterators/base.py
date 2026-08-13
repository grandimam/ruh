from typing import TypeVar

T = TypeVar("T")


class BaseIterator:
    def __init__(
        self,
        items: list[T],
        /,
        start: int = 0,
        end: int | None = None,
    ):
        self._items = items
        self._start = 0
        self._end = len(items) if end is None else end
        self._index = start

    def __iter__(self) -> "BaseIterator":
        return self

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int) -> None:
        self._index = value

    def __next__(self):
        if self._index >= self._end:
            raise StopIteration
        item = self._items[self._index]
        self._index += 1
        return item
