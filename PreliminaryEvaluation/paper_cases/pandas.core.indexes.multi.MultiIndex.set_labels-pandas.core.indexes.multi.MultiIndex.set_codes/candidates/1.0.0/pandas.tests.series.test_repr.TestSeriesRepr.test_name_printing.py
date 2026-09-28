def test_name_printing(self):
    s = Series([0, 1, 2])
    s.name = 'test'
    assert 'Name: test' in repr(s)
    s.name = None
    assert 'Name:' not in repr(s)
    s = Series(range(1000))
    s.name = 'test'
    assert 'Name: test' in repr(s)
    s.name = None
    assert 'Name:' not in repr(s)
    s = Series(index=date_range('20010101', '20020101'), name='test', dtype=object)
    assert 'Name: test' in repr(s)