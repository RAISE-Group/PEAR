def test_nunique_empty(self):
    df = DataFrame(columns=['a', 'b', 'c'])
    result = df.nunique()
    expected = Series(0, index=df.columns)
    tm.assert_series_equal(result, expected)
    result = df.T.nunique()
    expected = Series([], index=pd.Index([]), dtype=np.float64)
    tm.assert_series_equal(result, expected)