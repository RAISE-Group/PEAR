def test_strftime_nat(self):
    arr = DatetimeArray(DatetimeIndex(['2019-01-01', pd.NaT]))
    result = arr.strftime('%Y-%m-%d')
    expected = np.array(['2019-01-01', np.nan], dtype=object)
    tm.assert_numpy_array_equal(result, expected)