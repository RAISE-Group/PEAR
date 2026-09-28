def test_loc_getitem_dups(self):
    df = DataFrame(np.random.random_sample((20, 5)), index=['ABCDE'[x % 5] for x in range(20)])
    expected = df.loc['A', 0]
    result = df.loc[:, 0].loc['A']
    tm.assert_series_equal(result, expected)