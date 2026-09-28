@pytest.mark.parametrize('subtype', [None, 'interval', 'Interval'])
def test_construction_generic(self, subtype):
    i = IntervalDtype(subtype)
    assert i.subtype is None
    assert is_interval_dtype(i)