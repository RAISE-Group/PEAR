@pytest.mark.parametrize('subtype', [None, 'interval', 'Interval', 'int64', 'uint64', 'float64', 'complex128', 'datetime64', 'timedelta64', PeriodDtype('Q')])
def test_equality_generic(self, subtype):
    dtype = IntervalDtype(subtype)
    assert is_dtype_equal(dtype, 'interval')
    assert is_dtype_equal(dtype, IntervalDtype())