from typing import Callable
from collection.abc import Sequence

from ruh.executor import Executor
from ruh.iterator import SplitIterable

def map(func: Callable, items: Sequence):
    """
    Apply transformation to every item

    Args:
        func: transformation function to be applied
        items: sequence of items
    """
    executor = Executor(SplitIterable(items) func)
    executor.run()
