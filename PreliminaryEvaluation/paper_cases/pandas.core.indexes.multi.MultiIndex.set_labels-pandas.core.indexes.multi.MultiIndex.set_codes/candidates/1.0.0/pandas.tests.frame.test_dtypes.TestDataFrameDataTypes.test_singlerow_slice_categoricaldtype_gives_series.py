def test_singlerow_slice_categoricaldtype_gives_series(self):
    df = pd.DataFrame({'x': pd.Categorical('a b c d e'.split())})
    result = df.iloc[0]
    raw_cat = pd.Categorical(['a'], categories=['a', 'b', 'c', 'd', 'e'])
    expected = pd.Series(raw_cat, index=['x'], name=0, dtype='category')
    tm.assert_series_equal(result, expected)