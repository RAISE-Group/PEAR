def test_loc_reverse_assignment(self):
    data = [1, 2, 3, 4, 5, 6] + [None] * 4
    expected = Series(data, index=range(2010, 2020))
    result = pd.Series(index=range(2010, 2020), dtype=np.float64)
    result.loc[2015:2010:-1] = [6, 5, 4, 3, 2, 1]
    tm.assert_series_equal(result, expected)