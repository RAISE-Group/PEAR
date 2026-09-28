def test_check_dtype(self, data):
    dtype = data.dtype
    df = pd.DataFrame({'A': pd.Series(data, dtype=dtype), 'B': data, 'C': 'foo', 'D': 1})
    if dtype.name == 'Int64':
        expected = pd.Series([True, True, False, True], index=list('ABCD'))
    else:
        expected = pd.Series([True, True, False, False], index=list('ABCD'))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        result = df.dtypes == str(dtype)
    self.assert_series_equal(result, expected)
    expected = pd.Series([True, True, False, False], index=list('ABCD'))
    result = df.dtypes.apply(str) == str(dtype)
    self.assert_series_equal(result, expected)