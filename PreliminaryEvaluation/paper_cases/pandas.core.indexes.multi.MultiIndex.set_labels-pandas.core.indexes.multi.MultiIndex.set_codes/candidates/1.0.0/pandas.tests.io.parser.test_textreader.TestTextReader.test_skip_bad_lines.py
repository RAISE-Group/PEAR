def test_skip_bad_lines(self, capsys):
    data = 'a:b:c\nd:e:f\ng:h:i\nj:k:l:m\nl:m:n\no:p:q:r'
    reader = TextReader(StringIO(data), delimiter=':', header=None)
    msg = 'Error tokenizing data\\. C error: Expected 3 fields in line 4, saw 4'
    with pytest.raises(parser.ParserError, match=msg):
        reader.read()
    reader = TextReader(StringIO(data), delimiter=':', header=None, error_bad_lines=False, warn_bad_lines=False)
    result = reader.read()
    expected = {0: np.array(['a', 'd', 'g', 'l'], dtype=object), 1: np.array(['b', 'e', 'h', 'm'], dtype=object), 2: np.array(['c', 'f', 'i', 'n'], dtype=object)}
    assert_array_dicts_equal(result, expected)
    reader = TextReader(StringIO(data), delimiter=':', header=None, error_bad_lines=False, warn_bad_lines=True)
    reader.read()
    captured = capsys.readouterr()
    assert 'Skipping line 4' in captured.err
    assert 'Skipping line 6' in captured.err