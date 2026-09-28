def test_timedelta_arithmetic(self):
    data = Series(['nat', '32 days'], dtype='timedelta64[ns]')
    deltas = [timedelta(days=1), Timedelta(1, unit='D')]
    for delta in deltas:
        result_method = data.add(delta)
        result_operator = data + delta
        expected = Series(['nat', '33 days'], dtype='timedelta64[ns]')
        tm.assert_series_equal(result_operator, expected)
        tm.assert_series_equal(result_method, expected)
        result_method = data.sub(delta)
        result_operator = data - delta
        expected = Series(['nat', '31 days'], dtype='timedelta64[ns]')
        tm.assert_series_equal(result_operator, expected)
        tm.assert_series_equal(result_method, expected)
        result_method = data.div(delta)
        result_operator = data / delta
        expected = Series([np.nan, 32.0], dtype='float64')
        tm.assert_series_equal(result_operator, expected)
        tm.assert_series_equal(result_method, expected)