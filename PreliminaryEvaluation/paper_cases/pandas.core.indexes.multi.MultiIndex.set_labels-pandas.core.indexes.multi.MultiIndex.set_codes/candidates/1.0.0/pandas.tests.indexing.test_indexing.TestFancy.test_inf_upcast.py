def test_inf_upcast(self):
    df = DataFrame(columns=[0])
    df.loc[1] = 1
    df.loc[2] = 2
    df.loc[np.inf] = 3
    assert df.loc[np.inf, 0] == 3
    result = df.index
    expected = pd.Float64Index([1, 2, np.inf])
    tm.assert_index_equal(result, expected)
    df = DataFrame()
    df.loc[0, 0] = 1
    df.loc[1, 1] = 2
    df.loc[0, np.inf] = 3
    result = df.columns
    expected = pd.Float64Index([0, 1, np.inf])
    tm.assert_index_equal(result, expected)