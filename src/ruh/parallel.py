from typing import Callable
from collections.abc import Sequence

from ruh.runtime import Executor
from ruh.iterators import SplitIterable


def mapper(func: Callable, items: Sequence):
    """
    Apply transformation for items. It should use the Fork/Join to chunk the collections,
    perform the transformation, and return the results.

    Args:
        func: transformation function to be applied
        items: sequence of items

    Usage:
        from ruh.parallel import map

        items = [1, 2, 3]

        map(lambda x: x ** 2, items)
    """
    splitter = SplitIterable(items)
    executor = Executor(splitter, func)
    executor.run()
