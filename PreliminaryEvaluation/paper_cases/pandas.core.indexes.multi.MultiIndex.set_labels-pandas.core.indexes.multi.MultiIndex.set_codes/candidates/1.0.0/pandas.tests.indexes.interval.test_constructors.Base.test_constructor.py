@pytest.mark.parametrize('breaks', [[3, 14, 15, 92, 653], np.arange(10, dtype='int64'), Int64Index(range(-10, 11)), Float64Index(np.arange(20, 30, 0.5)), date_range('20180101', periods=10), date_range('20180101', periods=10, tz='US/Eastern'), timedelta_range('1 day', periods=10)])
def test_constructor(self, constructor, breaks, closed, name):
    result_kwargs = self.get_kwargs_from_breaks(breaks, closed)
    result = constructor(closed=closed, name=name, **result_kwargs)
    assert result.closed == closed
    assert result.name == name
    assert result.dtype.subtype == getattr(breaks, 'dtype', 'int64')
    tm.assert_index_equal(result.left, Index(breaks[:-1]))
    tm.assert_index_equal(result.right, Index(breaks[1:]))