@pytest.mark.parametrize('dtype,msg', [('m8[ps]', 'cannot convert timedeltalike'), ('M8[ps]', 'cannot convert datetimelike')])
def test_constructor_generic_timestamp_bad_frequency(self, dtype, msg):
    with pytest.raises(TypeError, match=msg):
        Series([], dtype=dtype)