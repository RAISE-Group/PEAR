def test_crosstab_no_overlap(self):
    s1 = pd.Series([1, 2, 3], index=[1, 2, 3])
    s2 = pd.Series([4, 5, 6], index=[4, 5, 6])
    actual = crosstab(s1, s2)
    expected = pd.DataFrame()
    tm.assert_frame_equal(actual, expected)