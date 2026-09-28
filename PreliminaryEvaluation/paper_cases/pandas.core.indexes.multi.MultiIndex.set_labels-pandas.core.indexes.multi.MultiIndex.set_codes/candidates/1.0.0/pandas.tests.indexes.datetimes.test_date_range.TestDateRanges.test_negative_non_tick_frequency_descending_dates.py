def test_negative_non_tick_frequency_descending_dates(self, tz_aware_fixture):
    tz = tz_aware_fixture
    result = pd.date_range(start='2011-06-01', end='2011-01-01', freq='-1MS', tz=tz)
    expected = pd.date_range(end='2011-06-01', start='2011-01-01', freq='1MS', tz=tz)[::-1]
    tm.assert_index_equal(result, expected)