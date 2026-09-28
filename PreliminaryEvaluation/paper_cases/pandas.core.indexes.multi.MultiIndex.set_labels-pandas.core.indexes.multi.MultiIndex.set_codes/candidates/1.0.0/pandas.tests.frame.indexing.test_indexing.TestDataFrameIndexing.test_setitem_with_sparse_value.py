def test_setitem_with_sparse_value(self):
    df = pd.DataFrame({'c_1': ['a', 'b', 'c'], 'n_1': [1.0, 2.0, 3.0]})
    sp_array = SparseArray([0, 0, 1])
    df['new_column'] = sp_array
    tm.assert_series_equal(df['new_column'], pd.Series(sp_array, name='new_column'), check_names=False)