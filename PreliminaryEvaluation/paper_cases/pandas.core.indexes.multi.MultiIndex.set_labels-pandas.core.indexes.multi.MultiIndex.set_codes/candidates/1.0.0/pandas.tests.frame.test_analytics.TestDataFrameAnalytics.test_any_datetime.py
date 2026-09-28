def test_any_datetime(self):
    float_data = [1, np.nan, 3, np.nan]
    datetime_data = [pd.Timestamp('1960-02-15'), pd.Timestamp('1960-02-16'), pd.NaT, pd.NaT]
    df = DataFrame({'A': float_data, 'B': datetime_data})
    result = df.any(1)
    expected = Series([True, True, True, False])
    tm.assert_series_equal(result, expected)