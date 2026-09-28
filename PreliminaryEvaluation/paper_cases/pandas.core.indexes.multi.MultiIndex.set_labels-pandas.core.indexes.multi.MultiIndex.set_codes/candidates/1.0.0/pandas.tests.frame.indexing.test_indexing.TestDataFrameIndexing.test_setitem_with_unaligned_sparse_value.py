def test_setitem_with_unaligned_sparse_value(self):
    df = pd.DataFrame({'c_1': ['a', 'b', 'c'], 'n_1': [1.0, 2.0, 3.0]})
    sp_series = pd.Series(SparseArray([0, 0, 1]), index=[2, 1, 0])
    df['new_column'] = sp_series
    exp = pd.Series(SparseArray([1, 0, 0]), name='new_column')
    tm.assert_series_equal(df['new_column'], exp)