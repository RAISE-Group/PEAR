def test_inplace_arithmetic(self):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    arr = self.array_cls(data, freq='D')
    expected = arr + pd.Timedelta(days=1)
    arr += pd.Timedelta(days=1)
    tm.assert_equal(arr, expected)
    expected = arr - pd.Timedelta(days=1)
    arr -= pd.Timedelta(days=1)
    tm.assert_equal(arr, expected)