def test_constructor_name(self):
    idx = date_range(start='2000-01-01', periods=1, freq='A', name='TEST')
    assert idx.name == 'TEST'