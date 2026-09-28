@pytest.mark.parametrize('metachar', ['[]', '()', '\\d', '\\w', '\\s'])
def test_replace_regex_metachar(self, metachar):
    df = DataFrame({'a': [metachar, 'else']})
    result = df.replace({'a': {metachar: 'paren'}})
    expected = DataFrame({'a': ['paren', 'else']})
    tm.assert_frame_equal(result, expected)