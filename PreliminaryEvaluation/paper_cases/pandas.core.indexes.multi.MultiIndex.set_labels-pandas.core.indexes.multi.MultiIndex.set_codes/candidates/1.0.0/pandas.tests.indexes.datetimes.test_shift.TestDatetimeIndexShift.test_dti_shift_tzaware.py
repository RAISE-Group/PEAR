def test_dti_shift_tzaware(self, tz_naive_fixture):
    tz = tz_naive_fixture
    idx = pd.DatetimeIndex([], name='xxx', tz=tz)
    tm.assert_index_equal(idx.shift(0, freq='H'), idx)
    tm.assert_index_equal(idx.shift(3, freq='H'), idx)
    idx = pd.DatetimeIndex(['2011-01-01 10:00', '2011-01-01 11:00', '2011-01-01 12:00'], name='xxx', tz=tz)
    tm.assert_index_equal(idx.shift(0, freq='H'), idx)
    exp = pd.DatetimeIndex(['2011-01-01 13:00', '2011-01-01 14:00', '2011-01-01 15:00'], name='xxx', tz=tz)
    tm.assert_index_equal(idx.shift(3, freq='H'), exp)
    exp = pd.DatetimeIndex(['2011-01-01 07:00', '2011-01-01 08:00', '2011-01-01 09:00'], name='xxx', tz=tz)
    tm.assert_index_equal(idx.shift(-3, freq='H'), exp)