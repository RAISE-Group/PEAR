@pytest.mark.parametrize('subtype', ['datetime64[ns]', 'timedelta64[ns]'])
def test_subtype_datetimelike(self, index, subtype):
    dtype = IntervalDtype(subtype)
    msg = 'Cannot convert .* to .*; subtypes are incompatible'
    with pytest.raises(TypeError, match=msg):
        index.astype(dtype)