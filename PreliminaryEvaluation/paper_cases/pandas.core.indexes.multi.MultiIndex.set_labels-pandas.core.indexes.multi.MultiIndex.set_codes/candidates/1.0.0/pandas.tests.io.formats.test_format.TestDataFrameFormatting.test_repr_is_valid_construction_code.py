def test_repr_is_valid_construction_code(self):
    idx = Index(['a', 'b'])
    res = eval('pd.' + repr(idx))
    tm.assert_series_equal(Series(res), Series(idx))