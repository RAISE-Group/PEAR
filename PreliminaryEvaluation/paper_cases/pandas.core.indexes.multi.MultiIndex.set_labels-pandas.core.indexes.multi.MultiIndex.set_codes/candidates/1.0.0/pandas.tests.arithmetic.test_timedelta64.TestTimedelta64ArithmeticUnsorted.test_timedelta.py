@pytest.mark.parametrize('freq', ['D', 'B'])
def test_timedelta(self, freq):
    index = pd.date_range('1/1/2000', periods=50, freq=freq)
    shifted = index + timedelta(1)
    back = shifted + timedelta(-1)
    tm.assert_index_equal(index, back)
    if freq == 'D':
        expected = pd.tseries.offsets.Day(1)
        assert index.freq == expected
        assert shifted.freq == expected
        assert back.freq == expected
    else:
        assert index.freq == pd.tseries.offsets.BusinessDay(1)
        assert shifted.freq is None
        assert back.freq == pd.tseries.offsets.BusinessDay(1)
    result = index - timedelta(1)
    expected = index + timedelta(-1)
    tm.assert_index_equal(result, expected)
    rng = pd.date_range('2013', '2014')
    s = Series(rng)
    result1 = rng - pd.offsets.Hour(1)
    result2 = DatetimeIndex(s - np.timedelta64(100000000))
    result3 = rng - np.timedelta64(100000000)
    result4 = DatetimeIndex(s - pd.offsets.Hour(1))
    tm.assert_index_equal(result1, result4)
    tm.assert_index_equal(result2, result3)