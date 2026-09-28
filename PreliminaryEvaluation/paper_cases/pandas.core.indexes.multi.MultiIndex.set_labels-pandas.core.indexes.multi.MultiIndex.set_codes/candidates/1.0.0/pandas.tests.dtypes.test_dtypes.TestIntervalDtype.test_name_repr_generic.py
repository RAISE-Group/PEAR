@pytest.mark.parametrize('subtype', [None, 'interval', 'Interval'])
def test_name_repr_generic(self, subtype):
    dtype = IntervalDtype(subtype)
    assert str(dtype) == 'interval'
    assert dtype.name == 'interval'