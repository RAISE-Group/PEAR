def test_indexing_zerodim_np_array(self):
    df = DataFrame([[1, 2], [3, 4]])
    result = df.iloc[np.array(0)]
    s = pd.Series([1, 2], name=0)
    tm.assert_series_equal(result, s)