@pytest.mark.xfail(reason='GH#15832')
def test_subtype_integer_errors(self):
    index = interval_range(-10.0, 10.0)
    dtype = IntervalDtype('uint64')
    with pytest.raises(ValueError):
        index.astype(dtype)
    index = interval_range(0.0, 10.0, freq=0.25)
    dtype = IntervalDtype('int64')
    with pytest.raises(ValueError):
        index.astype(dtype)
    dtype = IntervalDtype('uint64')
    with pytest.raises(ValueError):
        index.astype(dtype)