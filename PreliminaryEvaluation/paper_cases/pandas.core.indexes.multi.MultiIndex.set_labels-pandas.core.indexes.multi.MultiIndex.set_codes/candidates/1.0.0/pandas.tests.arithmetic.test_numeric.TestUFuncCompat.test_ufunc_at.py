def test_ufunc_at(self):
    s = pd.Series([0, 1, 2], index=[1, 2, 3], name='x')
    np.add.at(s, [0, 2], 10)
    expected = pd.Series([10, 1, 12], index=[1, 2, 3], name='x')
    tm.assert_series_equal(s, expected)