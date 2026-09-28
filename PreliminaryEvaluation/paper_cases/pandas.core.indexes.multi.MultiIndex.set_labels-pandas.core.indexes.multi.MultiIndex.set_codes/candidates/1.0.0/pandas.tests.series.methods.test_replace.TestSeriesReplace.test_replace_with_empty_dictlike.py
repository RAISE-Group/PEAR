def test_replace_with_empty_dictlike(self):
    s = pd.Series(list('abcd'))
    tm.assert_series_equal(s, s.replace(dict()))
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        empty_series = pd.Series([])
    tm.assert_series_equal(s, s.replace(empty_series))