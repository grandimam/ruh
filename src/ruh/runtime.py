from typing import Callable

from concurrent.futures import ThreadPoolExecutor


class Executor:
    MAX_WORKERS: int = 10

    def __init__(self, max_workers: int = MAX_WORKERS):
        self._workers = ThreadPoolExecutor(max_workers=max_workers)

    def run(self, itr: SplitIterable, func: Callable):
        it = iter(itr)
        q = [it]
        while q:
            item = q.pop()
            if item.remaining():
                l, r = item.split()
                q.append(l)
                q.append(r)
            else:
                self._workers.submit(func, next(item))
