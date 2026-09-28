@pytest.mark.parametrize('breaks, subtype', [(Int64Index([0, 1, 2, 3, 4]), 'float64'), (Int64Index([0, 1, 2, 3, 4]), 'datetime64[ns]'), (Int64Index([0, 1, 2, 3, 4]), 'timedelta64[ns]'), (Float64Index([0, 1, 2, 3, 4]), 'int64'), (date_range('2017-01-01', periods=5), 'int64'), (timedelta_range('1 day', periods=5), 'int64')])
def test_constructor_dtype(self, constructor, breaks, subtype):
    expected_kwargs = self.get_kwargs_from_breaks(breaks.astype(subtype))
    expected = constructor(**expected_kwargs)
    result_kwargs = self.get_kwargs_from_breaks(breaks)
    iv_dtype = IntervalDtype(subtype)
    for dtype in (iv_dtype, str(iv_dtype)):
        result = constructor(dtype=dtype, **result_kwargs)
        tm.assert_index_equal(result, expected)