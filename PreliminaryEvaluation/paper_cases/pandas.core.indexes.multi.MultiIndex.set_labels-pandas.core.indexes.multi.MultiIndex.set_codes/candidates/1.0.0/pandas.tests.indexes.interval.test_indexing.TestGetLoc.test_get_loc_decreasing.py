@pytest.mark.parametrize('values', [date_range('2018-01-04', periods=4, freq='-1D'), date_range('2018-01-04', periods=4, freq='-1D', tz='US/Eastern'), timedelta_range('3 days', periods=4, freq='-1D'), np.arange(3.0, -1.0, -1.0), np.arange(3, -1, -1)], ids=lambda x: str(x.dtype))
def test_get_loc_decreasing(self, values):
    index = IntervalIndex.from_arrays(values[1:], values[:-1])
    result = index.get_loc(index[0])
    expected = 0
    assert result == expected