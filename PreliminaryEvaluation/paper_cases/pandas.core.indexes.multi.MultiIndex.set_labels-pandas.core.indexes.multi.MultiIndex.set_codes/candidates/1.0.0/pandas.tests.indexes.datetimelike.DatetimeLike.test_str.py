def test_str(self):
    idx = self.create_index()
    idx.name = 'foo'
    assert not 'length={}'.format(len(idx)) in str(idx)
    assert "'foo'" in str(idx)
    assert type(idx).__name__ in str(idx)
    if hasattr(idx, 'tz'):
        if idx.tz is not None:
            assert idx.tz in str(idx)
    if hasattr(idx, 'freq'):
        assert "freq='{idx.freqstr}'".format(idx=idx) in str(idx)