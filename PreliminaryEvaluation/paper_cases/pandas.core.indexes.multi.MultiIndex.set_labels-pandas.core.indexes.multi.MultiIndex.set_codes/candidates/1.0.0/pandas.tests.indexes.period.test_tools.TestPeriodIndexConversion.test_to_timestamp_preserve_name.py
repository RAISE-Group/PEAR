def test_to_timestamp_preserve_name(self):
    index = period_range(freq='A', start='1/1/2001', end='12/1/2009', name='foo')
    assert index.name == 'foo'
    conv = index.to_timestamp('D')
    assert conv.name == 'foo'