def test_regex_replace_dict_nested_non_first_character(self):
    df = pd.DataFrame({'first': ['abc', 'bca', 'cab']})
    expected = pd.DataFrame({'first': ['.bc', 'bc.', 'c.b']})
    result = df.replace({'a': '.'}, regex=True)
    tm.assert_frame_equal(result, expected)