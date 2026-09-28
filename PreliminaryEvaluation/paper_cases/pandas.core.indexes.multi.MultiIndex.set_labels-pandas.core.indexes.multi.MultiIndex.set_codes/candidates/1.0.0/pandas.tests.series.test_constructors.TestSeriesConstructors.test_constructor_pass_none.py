def test_constructor_pass_none(self):
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        s = Series(None, index=range(5))
    assert s.dtype == np.float64
    s = Series(None, index=range(5), dtype=object)
    assert s.dtype == np.object_
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        s = Series(index=np.array([None]))
        expected = Series(index=Index([None]))
    tm.assert_series_equal(s, expected)