from typing import Callable
from collection.abc import Sequence

from ruh.executor import Executor
from ruh.iterator import SplitIterable

def map(func: Callable, items: Sequence):
    """
    Apply transformation for items

    Args:
        func: transformation function to be applied
        items: sequence of items

    Usage:
        from ruh.parallel import map

        items = [1, 2, 3]

        map(lambda x: x ** 2, items)
    """
    executor = Executor(SplitIterable(items) func)
    executor.run()
