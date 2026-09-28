def test_take_preserve_name(self):
    index = self._holder([1, 2, 3, 4], name='foo')
    taken = index.take([3, 0, 1])
    assert index.name == taken.name