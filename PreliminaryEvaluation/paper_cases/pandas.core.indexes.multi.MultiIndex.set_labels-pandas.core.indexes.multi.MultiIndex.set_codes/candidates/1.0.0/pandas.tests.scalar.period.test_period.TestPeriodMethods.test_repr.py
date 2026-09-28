def test_repr(self):
    p = Period('Jan-2000')
    assert '2000-01' in repr(p)
    p = Period('2000-12-15')
    assert '2000-12-15' in repr(p)