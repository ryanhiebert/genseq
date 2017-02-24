from __future__ import unicode_literals
from genseq import genseq, Genseq


class TestGenseq(object):
    def test_iterable_preserve(self):
        """Should preserve the contents of the iterable."""
        assert list(Genseq('abcdef')) == list('abcdef')

    def test_lazy_index(self):
        """Should only consume to the index needed."""
        it = iter(list('abcdef'))
        seq = Genseq(it)
        assert seq[3] == 'd'
        assert list(it) == list('ef')
        assert list(seq) == list('abcd')

    def test_lazy_slice(self):
        """Should only consume to the index needed."""
        it = iter(list('abcdef'))
        seq = Genseq(it)
        assert list(seq[1:4]) == list('bcd')
        assert list(it) == list('ef')
        assert list(seq) == list('abcd')

    def test_lazy_slice_step(self):
        """Should only consume to the index needed."""
        it = iter(list('abcdef'))
        seq = Genseq(it)
        assert list(seq[1:4:2]) == list('bd')
        assert list(it) == list('ef')
        assert list(seq) == list('abcd')

    def test_slice_negative_start(self):
        """Should fully consume the iterator when start is negative."""
        it = iter(list('abcdef'))
        seq = Genseq(it)
        assert list(seq[-5:4]) == list('bcd')
        assert list(it) == []
        assert list(seq) == list('abcdef')

    def test_slice_negative_stop(self):
        """Should fully consume the iterator when stop is negative."""
        it = iter(list('abcdef'))
        seq = Genseq(it)
        assert list(seq[1:-2]) == list('bcd')
        assert list(it) == []
        assert list(seq) == list('abcdef')

    def test_slice_negative_step(self):
        """Should fully consume the iterator when step is negative."""
        it = iter(list('abcdef'))
        seq = Genseq(it)
        assert list(seq[:2:-2]) == list('fd')
        assert list(it) == []
        assert list(seq) == list('abcdef')

    def test_len(self):
        """Should fully consume the iterator."""
        it = iter(list('abcdef'))
        seq = Genseq(it)
        assert len(seq) == 6
        assert list(it) == []
        assert list(seq) == list('abcdef')

    def test_repr(self):
        """Should show a maximum of 10 items, with indicator if more."""
        assert repr(Genseq('abcdef')).count(',') == 5
        assert repr(Genseq('abcdefghij')).count(',') == 9
        assert repr(Genseq('abcdefghijk')).count(',') == 10
        assert ', ...' in repr(Genseq('abcdefghijk'))
        assert repr(Genseq('abcdefghijkl')).count(',') == 10
        assert ', ...' in repr(Genseq('abcdefghijkl'))

    def test_decorator(self):
        """The decorator should make a generator return a Genseq."""
        @genseq
        def mygen(stop):
            for i in range(stop):
                yield i
        assert isinstance(mygen(5), Genseq)
        assert list(mygen(5)) == list(range(5))
