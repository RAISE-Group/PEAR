def test_astype_datetime64(self):
    idx = DatetimeIndex(['2016-05-16', 'NaT', NaT, np.NaN])
    result = idx.astype('datetime64[ns]')
    tm.assert_index_equal(result, idx)
    assert result is not idx
    result = idx.astype('datetime64[ns]', copy=False)
    tm.assert_index_equal(result, idx)
    assert result is idx
    idx_tz = DatetimeIndex(['2016-05-16', 'NaT', NaT, np.NaN], tz='EST')
    result = idx_tz.astype('datetime64[ns]')
    expected = DatetimeIndex(['2016-05-16 05:00:00', 'NaT', 'NaT', 'NaT'], dtype='datetime64[ns]')
    tm.assert_index_equal(result, expected)