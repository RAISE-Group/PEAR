@pytest.mark.parametrize('dtype', [np.datetime64, np.timedelta64])
def test_astype_generic_timestamp_no_frequency(self, dtype):
    data = [1]
    s = Series(data)
    msg = "The '{dtype}' dtype has no unit\\. Please pass in '{dtype}\\[ns\\]' instead.".format(dtype=dtype.__name__)
    with pytest.raises(ValueError, match=msg):
        s.astype(dtype)