def test_subsets_multiindex_dtype(self):
    data = [['x', 1]]
    columns = [('a', 'b', np.nan), ('a', 'c', 0.0)]
    df = DataFrame(data, columns=pd.MultiIndex.from_tuples(columns))
    expected = df.dtypes.a.b
    result = df.a.b.dtypes
    tm.assert_series_equal(result, expected)