def test_identical(self, left):
    merged = pd.merge(left, left, on='X')
    result = merged.dtypes.sort_index()
    expected = Series([CategoricalDtype(), np.dtype('O'), np.dtype('O')], index=['X', 'Y_x', 'Y_y'])
    tm.assert_series_equal(result, expected)