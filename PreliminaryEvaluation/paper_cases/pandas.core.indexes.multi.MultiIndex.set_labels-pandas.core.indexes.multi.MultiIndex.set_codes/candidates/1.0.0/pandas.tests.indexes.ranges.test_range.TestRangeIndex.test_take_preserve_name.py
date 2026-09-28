def test_take_preserve_name(self):
    index = RangeIndex(1, 5, name='foo')
    taken = index.take([3, 0, 1])
    assert index.name == taken.name