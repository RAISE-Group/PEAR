def test_diff_int(self):
    a = 10000000000000000
    b = a + 1
    s = Series([a, b])
    result = s.diff()
    assert result[1] == 1