from ruh.splitter import SplitIterable
from ruh.splitter import _Iterator

def test_create_split_iterable_success():
    iterable = SplitIterable[int](items = [1, 2, 3, 4])
    it = iter(iterable)
    assert type(it) == _Iterator
