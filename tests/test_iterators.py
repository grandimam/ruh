import pytest

from ruh.iterators import IndexIterator
from ruh.iterators import RangeIterator
from ruh.iterators import ReverseIterator


def test_index_iterable_success():
    it = IndexIterator([1, 2, 3, 4])
    assert list(it) == [1, 2, 3, 4]


def test_index_iterable_none():
    with pytest.raises(TypeError):
        IndexIterator(items=None)


def test_reverse_iterable_success():
    it = ReverseIterator([1, 2, 3, 4])
    assert list(it) == [4, 3, 2, 1]


def test_range_iterator_success():
    it = RangeIterator(start=0, end=10, step=2)
    assert list(it) == [2, 4, 6, 8, 10]
