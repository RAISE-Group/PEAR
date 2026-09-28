def test_to_string_with_formatters_unicode(self):
    df = DataFrame({'c/σ': [1, 2, 3]})
    result = df.to_string(formatters={'c/σ': str})
    assert result == '  c/σ\n' + '0   1\n1   2\n2   3'