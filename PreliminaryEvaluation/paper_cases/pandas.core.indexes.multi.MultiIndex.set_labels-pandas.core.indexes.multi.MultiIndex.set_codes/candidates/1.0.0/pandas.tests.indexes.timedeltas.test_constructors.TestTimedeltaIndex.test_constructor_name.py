def test_constructor_name(self):
    idx = timedelta_range(start='1 days', periods=1, freq='D', name='TEST')
    assert idx.name == 'TEST'
    idx2 = TimedeltaIndex(idx, name='something else')
    assert idx2.name == 'something else'