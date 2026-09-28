def test_constructor_series(self):
    index1 = ['d', 'b', 'a', 'c']
    index2 = sorted(index1)
    s1 = Series([4, 7, -5, 3], index=index1)
    s2 = Series(s1, index=index2)
    tm.assert_series_equal(s2, s1.sort_index())