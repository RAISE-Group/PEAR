def test_getitem_sparse_column(self):
    data = SparseArray([0, 1])
    df = pd.DataFrame({'A': data})
    expected = pd.Series(data, name='A')
    result = df['A']
    tm.assert_series_equal(result, expected)
    result = df.iloc[:, 0]
    tm.assert_series_equal(result, expected)
    result = df.loc[:, 'A']
    tm.assert_series_equal(result, expected)