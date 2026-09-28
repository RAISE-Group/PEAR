def test_to_string_length(self):
    s = Series(range(100), dtype='int64')
    res = s.to_string(max_rows=2, length=True)
    exp = '0      0\n      ..\n99    99\nLength: 100'
    assert res == exp