def test_asarray_tz_aware(self):
    tz = 'US/Central'
    idx = pd.date_range('2000', periods=2, tz=tz)
    expected = np.array(['2000-01-01T06', '2000-01-02T06'], dtype='M8[ns]')
    result = np.asarray(idx, dtype='datetime64[ns]')
    tm.assert_numpy_array_equal(result, expected)
    result = np.asarray(idx, dtype='M8[ns]')
    tm.assert_numpy_array_equal(result, expected)
    expected = np.array([pd.Timestamp('2000-01-01', tz=tz), pd.Timestamp('2000-01-02', tz=tz)])
    result = np.asarray(idx, dtype=object)
    tm.assert_numpy_array_equal(result, expected)