from ruh.iterator import SplitIterable
from typing import Callable

from concurrent.futures import ThreadPoolExecutor

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
