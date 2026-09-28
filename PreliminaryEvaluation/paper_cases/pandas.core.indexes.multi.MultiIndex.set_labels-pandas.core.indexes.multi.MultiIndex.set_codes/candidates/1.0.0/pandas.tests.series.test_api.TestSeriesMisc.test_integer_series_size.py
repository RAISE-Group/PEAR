def test_integer_series_size(self):
    s = Series(range(9))
    assert s.size == 9
    s = Series(range(9), dtype='Int64')
    assert s.size == 9