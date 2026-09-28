def test_slice_duplicate_monotonic(self):
    idx = pd.DatetimeIndex(['2017', '2017'])
    result = idx._maybe_cast_slice_bound('2017-01-01', 'left', 'loc')
    expected = Timestamp('2017-01-01')
    assert result == expected