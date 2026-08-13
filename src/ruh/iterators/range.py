class _Iterator:
    def __init__(self, start, end, step=1):
        self._start = start
        self._end = end
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self._start >= self._end:
            raise StopIteration
        if self._step > 0:
            self._start += self._step
        return self._start


class RangeIterator:
    def __init__(self, start: int = 0, end: int = 0, step: int = 1):
        self._start = start
        self._end = end
        self._step = step

    def __iter__(self):
        return _Iterator(start=self._start, end=self._end, step=self._step)
