===================================
Genseq: A Lazily Resolving Sequence
===================================

.. image:: https://img.shields.io/pypi/v/genseq/badge/?version=stable
   :target: https://pypi.python.org/pypi/genseq
   :alt: Latest version

.. image:: https://travis-ci.org/ryanhiebert/genseq.svg?branch=master
   :target: https://travis-ci.org/ryanhiebert/genseq

Genseq is sequence data structure that lazily consumes any iterable,
including a generator, so that you can enjoy the benefits of both
delayed evaluation, and the slicing and random access of lists.

The ``Genseq`` class implements the collections ``Sequence`` ABC,
so the standard methods of using an immutable sequence are all available.

Usage
=====

Install using Pip:

.. code-block:: sh

    pip install genseq

Then wrap your generator with ``genseq``:

.. code-block:: pycon

    >>> from genseq import genseq
    >>> @genseq
    ... def myiter(stop):
    ...     for i in range(stop):
    ...         yield i
    ...
    >>> myiter(5)[2]
    2
    >>>

Or use the ``Genseq`` class on any iterable:

.. code-block:: pycon

   >>> from genseq import Genseq
   >>> Genseq(range(5))[3]
   3
   >>>

Happy indexing!
