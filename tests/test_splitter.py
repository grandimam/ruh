from ruh.splitter import SplitIterable
from ruh.splitter import _Iterator


def test_create_split_iterable_success():
    iterable = SplitIterable[int](items=[1, 2, 3, 4])
    it = iter(iterable)
    assert type(it) == _Iterator


def test_split_iterable_create_chunks():
    iterable = SplitIterable[int](items=[1, 2, 3, 4])
    it = iter(iterable)
    l, r = it.split()
    assert list(l) == [1, 2]
    assert list(r) == [3, 4]
