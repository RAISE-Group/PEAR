def test_repr_min_rows(self):
    s = pd.Series(range(20))
    assert '..' not in repr(s)
    s = pd.Series(range(61))
    assert '..' in repr(s)
    with option_context('display.max_rows', 10, 'display.min_rows', 4):
        assert '..' in repr(s)
        assert '2  ' not in repr(s)
    with option_context('display.max_rows', 12, 'display.min_rows', None):
        assert '5      5' in repr(s)
    with option_context('display.max_rows', 10, 'display.min_rows', 12):
        assert '5      5' not in repr(s)
    with option_context('display.max_rows', None, 'display.min_rows', 12):
        assert '..' not in repr(s)