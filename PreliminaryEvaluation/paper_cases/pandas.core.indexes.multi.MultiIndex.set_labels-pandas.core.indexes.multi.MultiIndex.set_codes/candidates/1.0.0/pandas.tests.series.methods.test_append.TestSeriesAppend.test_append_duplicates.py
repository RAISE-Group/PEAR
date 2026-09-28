def test_append_duplicates(self):
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5, 6])
    exp = pd.Series([1, 2, 3, 4, 5, 6], index=[0, 1, 2, 0, 1, 2])
    tm.assert_series_equal(s1.append(s2), exp)
    tm.assert_series_equal(pd.concat([s1, s2]), exp)
    exp = pd.Series([1, 2, 3, 4, 5, 6])
    tm.assert_series_equal(s1.append(s2, ignore_index=True), exp, check_index_type=True)
    tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp, check_index_type=True)
    msg = 'Indexes have overlapping values:'
    with pytest.raises(ValueError, match=msg):
        s1.append(s2, verify_integrity=True)
    with pytest.raises(ValueError, match=msg):
        pd.concat([s1, s2], verify_integrity=True)