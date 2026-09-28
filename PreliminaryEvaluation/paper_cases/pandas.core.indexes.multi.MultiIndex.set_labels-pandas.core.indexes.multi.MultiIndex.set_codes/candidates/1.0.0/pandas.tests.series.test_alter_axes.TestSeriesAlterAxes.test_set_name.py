def test_set_name(self):
    s = Series([1, 2, 3])
    s2 = s._set_name('foo')
    assert s2.name == 'foo'
    assert s.name is None
    assert s is not s2