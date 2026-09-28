def test_quantile_sparse(self):
    s = pd.Series(pd.arrays.SparseArray([1, 2]))
    s1 = pd.Series(pd.arrays.SparseArray([3, 4]))
    df = pd.DataFrame({0: s, 1: s1})
    result = df.quantile()
    expected = pd.Series([1.5, 3.5], name=0.5)
    tm.assert_series_equal(result, expected)