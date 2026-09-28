def test_basic(self, left, right):
    merged = pd.merge(left, right, on='X')
    result = merged.dtypes.sort_index()
    expected = Series([CategoricalDtype(), np.dtype('O'), np.dtype('int64')], index=['X', 'Y', 'Z'])
    tm.assert_series_equal(result, expected)