def test_series_partial_set_datetime(self):
    idx = date_range('2011-01-01', '2011-01-02', freq='D', name='idx')
    ser = Series([0.1, 0.2], index=idx, name='s')
    result = ser.loc[[Timestamp('2011-01-01'), Timestamp('2011-01-02')]]
    exp = Series([0.1, 0.2], index=idx, name='s')
    tm.assert_series_equal(result, exp, check_index_type=True)
    keys = [Timestamp('2011-01-02'), Timestamp('2011-01-02'), Timestamp('2011-01-01')]
    exp = Series([0.2, 0.2, 0.1], index=pd.DatetimeIndex(keys, name='idx'), name='s')
    tm.assert_series_equal(ser.loc[keys], exp, check_index_type=True)
    keys = [Timestamp('2011-01-03'), Timestamp('2011-01-02'), Timestamp('2011-01-03')]
    with pytest.raises(KeyError, match='with any missing labels'):
        ser.loc[keys]