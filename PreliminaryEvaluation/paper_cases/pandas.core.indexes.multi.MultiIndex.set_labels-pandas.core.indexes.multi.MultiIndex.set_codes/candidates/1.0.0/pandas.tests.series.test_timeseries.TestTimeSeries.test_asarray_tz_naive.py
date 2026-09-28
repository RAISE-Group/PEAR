def test_asarray_tz_naive(self):
    ser = pd.Series(pd.date_range('2000', periods=2))
    expected = np.array(['2000-01-01', '2000-01-02'], dtype='M8[ns]')
    result = np.asarray(ser)
    tm.assert_numpy_array_equal(result, expected)
    result = np.asarray(ser, dtype=object)
    expected = np.array([pd.Timestamp('2000-01-01'), pd.Timestamp('2000-01-02')])
    tm.assert_numpy_array_equal(result, expected)