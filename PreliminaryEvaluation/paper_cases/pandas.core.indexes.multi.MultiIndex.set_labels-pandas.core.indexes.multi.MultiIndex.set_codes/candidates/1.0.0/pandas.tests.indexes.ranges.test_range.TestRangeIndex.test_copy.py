def test_copy(self):
    i = RangeIndex(5, name='Foo')
    i_copy = i.copy()
    assert i_copy is not i
    assert i_copy.identical(i)
    assert i_copy._range == range(0, 5, 1)
    assert i_copy.name == 'Foo'