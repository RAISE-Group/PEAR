def test_set_value_by_index(self):
    df = DataFrame(np.arange(9).reshape(3, 3).T)
    df.columns = list('AAA')
    expected = df.iloc[:, 2]
    df.iloc[:, 0] = 3
    tm.assert_series_equal(df.iloc[:, 2], expected)
    df = DataFrame(np.arange(9).reshape(3, 3).T)
    df.columns = [2, float(2), str(2)]
    expected = df.iloc[:, 1]
    df.iloc[:, 0] = 3
    tm.assert_series_equal(df.iloc[:, 1], expected)