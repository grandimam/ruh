import pytest

from ruh.iterators import IndexIterator
from ruh.iterators import RangeIterator
from ruh.iterators import ReverseIterator
from ruh.iterators import FixedSizedSplitIterator


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

def test_fixed_size_iterator_success():
    f_it = FixedSizedSplitIterator(items=list(range(10)), max_size=3)
    l, r = iter(f_it).split()
    assert list(l) == [0, 1, 2]
    assert list(r) == [3, 4, 5, 6, 7, 8, 9]

def test_fixed_size_iterator_raises_error():
    f_it = FixedSizedSplitIterator(items=list(range(10)), max_size=3)
    l, _ = iter(f_it).split()
    with pytest.raises(StopIteration):
        _, _ = iter(l).split()
