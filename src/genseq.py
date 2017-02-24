from functools import wraps
from itertools import islice
try:
    from collections.abc import Sequence
except ImportError:
    from collections import Sequence  # Python 2


def genseq(fn):
    """Wrap an iterable-returning function to return an Uberseq.

    The most common use for this decorator is to wrap a generator
    function. For example:

    .. code-block:: python

        @genseq
        def to(count):
            for i in range(count):
                yield i
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return Genseq(fn(*args, **kwargs))
    return wrapper


class Genseq(Sequence):
    """A lazy sequence generated from an arbitrary iterable.

    The arbitrary may be, and is expected to often be, a generator
    or other lazily evaluated iterable.
    """
    def __init__(self, iterable):
        self.__iter = iter(iterable)
        self.__exhausted = False
        self.__resolved = []
        self.__len = 0

    def __advance(self, to=None):
        """Exhaust the iterator to the given positive index."""
        if not self.__exhausted:
            stop = None if to is None else max(to - self.__len, 0)
            items = list(islice(self.__iter, stop))
            self.__resolved.extend(items)
            self.__len += len(items)
            self.__exhausted = stop is None or len(items) < stop

    def __getitem__(self, index):
        """Get the item at the given index.

        Continue to exhaust the iterator as necessary. Slices and
        negative indexes are allowed, but any negative index or
        slice component will exhaust the iterator.
        """
        if isinstance(index, slice):
            if min(index.start or 0, index.stop or 0, index.step or 0) < 0:
                self.__advance()  # Negative indexing requires exhaustion
                return type(self)(self.__resolved[index])
            return type(self)(
                islice(iter(self), index.start, index.stop, index.step))
        self.__advance(None if index < 0 else index + 1)
        return self.__resolved[index]

    def __len__(self):
        """Find the length of the iterable.

        Ensure that the iterable is exhausted, then return then length.
        """
        self.__advance()
        return self.__len

    def __repr__(self):
        """Show a representation of this sequence."""
        items = list(self[:11])
        items_repr = repr(items[:10])
        if len(items) == 11:
            items_repr = items_repr[:-1] + ', ...' + items_repr[-1:]
        return items_repr
