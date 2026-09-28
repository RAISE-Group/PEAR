def test_xs_duplicates(self):
    df = DataFrame(np.random.randn(5, 2), index=['b', 'b', 'c', 'b', 'a'])
    cross = df.xs('c')
    exp = df.iloc[2]
    tm.assert_series_equal(cross, exp)