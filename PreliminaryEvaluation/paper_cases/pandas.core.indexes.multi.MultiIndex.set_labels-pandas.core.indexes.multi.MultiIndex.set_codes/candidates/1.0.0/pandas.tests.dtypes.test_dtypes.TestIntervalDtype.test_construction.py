@pytest.mark.parametrize('subtype', ['interval[int64]', 'Interval[int64]', 'int64', np.dtype('int64')])
def test_construction(self, subtype):
    i = IntervalDtype(subtype)
    assert i.subtype == np.dtype('int64')
    assert is_interval_dtype(i)