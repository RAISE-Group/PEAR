def test_construction_from_string(self):
    result = DatetimeTZDtype.construct_from_string('datetime64[ns, US/Eastern]')
    assert is_dtype_equal(self.dtype, result)
    msg = "Cannot construct a 'DatetimeTZDtype' from 'foo'"
    with pytest.raises(TypeError, match=msg):
        DatetimeTZDtype.construct_from_string('foo')