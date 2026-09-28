def test_repeat(self):
    s = Series(np.random.randn(3), index=['a', 'b', 'c'])
    reps = s.repeat(5)
    exp = Series(s.values.repeat(5), index=s.index.values.repeat(5))
    tm.assert_series_equal(reps, exp)
    to_rep = [2, 3, 4]
    reps = s.repeat(to_rep)
    exp = Series(s.values.repeat(to_rep), index=s.index.values.repeat(to_rep))
    tm.assert_series_equal(reps, exp)