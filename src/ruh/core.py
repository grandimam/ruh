from typing import Callable
from typing import TypeVar

from concurrent.futures import ThreadPoolExecutor

T = TypeVar("T")

class Executor:

    MAX_WORKERS: int = 10

    def __init__(
        self,
        iterable: SplitIterable,
        func: Callable,
        max_workers: int = MAX_WORKERS
    ):
        self._iterable = iterable
        self._func = func
        self._workers = ThreadPoolExecutor(max_workers = max_workers)


    def run(self):
        it = iter(self._iterable)
        q = [it]
        while q:
            item = q.pop()
            if item.remaining():
                l, r = item.split()
                q.append(l)
                q.append(r)
            else:
                self._workers.submit(self._func, next(item))

class SplitIterable[T]:

    def __init__(self, items: list[T]) -> None:
        self._items = items

    def __iter__(self) -> None:
        return _SplitIterator(self)

    @property
    def items(self) -> int:
        return self._items

class _Iterator:

    def __init__(
        self,
        iterable: SplitIterable,
        start: int = 0
        end: int = None
    ):
        self._it = iterable
        self._start = 0
        self._end = len(self._it.items) if end is None else end
        self._index = start

    def __iter__(self) -> _Iterator:
        return self

    def __next__(self):
        if self._index >= self._end:
            raise StopIteration
        item = self._it.items[self._index]
        self._index += 1
        return item

    def remaining(self):
        return self._end - self._index

    def split(self):
        mid = (self._start + self._end) // 2
        left = _Iterator(self._it, self._start, mid)
        right = _Iterator(self._it, mid, self._end)
        return left, right
