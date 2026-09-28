def test_interval_index(self):
    index = pd.interval_range(start=0, periods=3)
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=index, columns=['A', 'B', 'C'])
    expected = 1
    result = df.loc[0.5, 'A']
    tm.assert_almost_equal(result, expected)
    index = pd.interval_range(start=0, periods=3, closed='both')
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=index, columns=['A', 'B', 'C'])
    index_exp = pd.interval_range(start=0, periods=2, freq=1, closed='both')
    expected = pd.Series([1, 4], index=index_exp, name='A')
    result = df.loc[1, 'A']
    tm.assert_series_equal(result, expected)