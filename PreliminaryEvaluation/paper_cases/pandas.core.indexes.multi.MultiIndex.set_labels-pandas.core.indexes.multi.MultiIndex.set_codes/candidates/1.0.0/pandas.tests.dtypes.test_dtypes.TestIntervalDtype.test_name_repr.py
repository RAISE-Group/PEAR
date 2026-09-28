@pytest.mark.parametrize('subtype', ['int64', 'uint64', 'float64', 'complex128', 'datetime64', 'timedelta64', PeriodDtype('Q')])
def test_name_repr(self, subtype):
    dtype = IntervalDtype(subtype)
    expected = f'interval[{subtype}]'
    assert str(dtype) == expected
    assert dtype.name == 'interval'