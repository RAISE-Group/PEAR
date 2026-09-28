@pytest.mark.xfail(reason='GH#15832')
def test_subtype_integer_errors(self):
    index = interval_range(-10, 10)
    dtype = IntervalDtype('uint64')
    with pytest.raises(ValueError):
        index.astype(dtype)