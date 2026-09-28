def test_merge_nocopy(self):
    left = DataFrame({'a': 0, 'b': 1}, index=range(10))
    right = DataFrame({'c': 'foo', 'd': 'bar'}, index=range(10))
    merged = merge(left, right, left_index=True, right_index=True, copy=False)
    merged['a'] = 6
    assert (left['a'] == 6).all()
    merged['d'] = 'peekaboo'
    assert (right['d'] == 'peekaboo').all()