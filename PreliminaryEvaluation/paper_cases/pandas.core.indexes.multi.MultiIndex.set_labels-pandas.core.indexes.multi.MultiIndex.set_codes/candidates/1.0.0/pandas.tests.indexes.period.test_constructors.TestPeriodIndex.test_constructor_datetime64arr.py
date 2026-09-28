def test_constructor_datetime64arr(self):
    vals = np.arange(100000, 100000 + 10000, 100, dtype=np.int64)
    vals = vals.view(np.dtype('M8[us]'))
    msg = 'Wrong dtype: datetime64\\[us\\]'
    with pytest.raises(ValueError, match=msg):
        PeriodIndex(vals, freq='D')