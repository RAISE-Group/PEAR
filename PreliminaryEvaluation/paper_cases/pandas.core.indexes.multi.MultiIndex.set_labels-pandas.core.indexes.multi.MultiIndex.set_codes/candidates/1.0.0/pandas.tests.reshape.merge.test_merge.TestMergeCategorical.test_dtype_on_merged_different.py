@pytest.mark.parametrize('change', [lambda x: x, lambda x: x.astype(CDT(['foo', 'bar', 'bah'])), lambda x: x.astype(CDT(ordered=True))])
def test_dtype_on_merged_different(self, change, join_type, left, right):
    X = change(right.X.astype('object'))
    right = right.assign(X=X)
    assert is_categorical_dtype(left.X.values)
    merged = pd.merge(left, right, on='X', how=join_type)
    result = merged.dtypes.sort_index()
    expected = Series([np.dtype('O'), np.dtype('O'), np.dtype('int64')], index=['X', 'Y', 'Z'])
    tm.assert_series_equal(result, expected)