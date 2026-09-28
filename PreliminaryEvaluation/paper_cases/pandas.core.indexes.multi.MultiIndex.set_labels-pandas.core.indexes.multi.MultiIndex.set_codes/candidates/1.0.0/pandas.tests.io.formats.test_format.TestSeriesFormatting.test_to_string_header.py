def test_to_string_header(self):
    s = pd.Series(range(10), dtype='int64')
    s.index.name = 'foo'
    res = s.to_string(header=True, max_rows=2)
    exp = 'foo\n0    0\n    ..\n9    9'
    assert res == exp
    res = s.to_string(header=False, max_rows=2)
    exp = '0    0\n    ..\n9    9'
    assert res == exp