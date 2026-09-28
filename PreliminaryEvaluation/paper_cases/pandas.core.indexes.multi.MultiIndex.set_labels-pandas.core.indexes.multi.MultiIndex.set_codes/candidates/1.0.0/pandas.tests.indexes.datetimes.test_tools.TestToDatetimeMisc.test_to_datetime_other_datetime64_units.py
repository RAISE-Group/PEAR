def test_to_datetime_other_datetime64_units(self):
    scalar = np.int64(1337904000000000).view('M8[us]')
    as_obj = scalar.astype('O')
    index = DatetimeIndex([scalar])
    assert index[0] == scalar.astype('O')
    value = Timestamp(scalar)
    assert value == as_obj