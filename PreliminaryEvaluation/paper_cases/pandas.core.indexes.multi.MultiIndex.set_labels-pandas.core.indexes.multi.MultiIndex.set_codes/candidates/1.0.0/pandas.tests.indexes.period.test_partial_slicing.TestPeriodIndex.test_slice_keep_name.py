def test_slice_keep_name(self):
    idx = period_range('20010101', periods=10, freq='D', name='bob')
    assert idx.name == idx[1:].name