def test_construction_with_mixed(self, float_string_frame):
    data = [[datetime(2001, 1, 5), np.nan, datetime(2001, 1, 2)], [datetime(2000, 1, 2), datetime(2000, 1, 3), datetime(2000, 1, 1)]]
    df = DataFrame(data)
    result = df.dtypes
    expected = Series({'datetime64[ns]': 3})
    float_string_frame['datetime'] = datetime.now()
    float_string_frame['timedelta'] = timedelta(days=1, seconds=1)
    assert float_string_frame['datetime'].dtype == 'M8[ns]'
    assert float_string_frame['timedelta'].dtype == 'm8[ns]'
    result = float_string_frame.dtypes
    expected = Series([np.dtype('float64')] * 4 + [np.dtype('object'), np.dtype('datetime64[ns]'), np.dtype('timedelta64[ns]')], index=list('ABCD') + ['foo', 'datetime', 'timedelta'])
    tm.assert_series_equal(result, expected)