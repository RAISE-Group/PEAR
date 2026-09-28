def test_other_columns(self, left, right):
    right = right.assign(Z=right.Z.astype('category'))
    merged = pd.merge(left, right, on='X')
    result = merged.dtypes.sort_index()
    expected = Series([CategoricalDtype(), np.dtype('O'), CategoricalDtype()], index=['X', 'Y', 'Z'])
    tm.assert_series_equal(result, expected)
    assert left.X.values.is_dtype_equal(merged.X.values)
    assert right.Z.values.is_dtype_equal(merged.Z.values)