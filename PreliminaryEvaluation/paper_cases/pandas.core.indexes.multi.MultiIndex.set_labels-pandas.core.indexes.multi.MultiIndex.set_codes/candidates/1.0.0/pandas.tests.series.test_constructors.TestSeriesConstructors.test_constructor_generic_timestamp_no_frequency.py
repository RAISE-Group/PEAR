@pytest.mark.parametrize('dtype', [np.datetime64, np.timedelta64])
def test_constructor_generic_timestamp_no_frequency(self, dtype):
    msg = 'dtype has no unit. Please pass in'
    with pytest.raises(ValueError, match=msg):
        Series([], dtype=dtype)