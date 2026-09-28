@pytest.mark.parametrize('freq', ['M', 'Q', 'A', 'D', 'B', 'BH', 'T', 'S', 'L', 'U', 'H', 'N', 'C'])
def test_from_freq_recreate_from_data(self, freq):
    org = date_range(start='2001/02/01 09:00', freq=freq, periods=1)
    idx = DatetimeIndex(org, freq=freq)
    tm.assert_index_equal(idx, org)
    org = date_range(start='2001/02/01 09:00', freq=freq, tz='US/Pacific', periods=1)
    idx = DatetimeIndex(org, freq=freq, tz='US/Pacific')
    tm.assert_index_equal(idx, org)