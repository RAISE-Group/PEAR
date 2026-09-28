def test_replace_replacer_equals_replacement(self):
    s = pd.Series(['a', 'b'])
    expected = pd.Series(['b', 'a'])
    result = s.replace({'a': 'b', 'b': 'a'})
    tm.assert_series_equal(expected, result)