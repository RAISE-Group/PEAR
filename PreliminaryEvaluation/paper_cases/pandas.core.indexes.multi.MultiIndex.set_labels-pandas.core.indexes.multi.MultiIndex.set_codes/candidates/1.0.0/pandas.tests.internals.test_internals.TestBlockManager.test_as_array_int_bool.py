def test_as_array_int_bool(self):
    mgr = create_mgr('a: bool-1; b: bool-2')
    assert mgr.as_array().dtype == np.bool_
    mgr = create_mgr('a: i8-1; b: i8-2; c: i4; d: i2; e: u1')
    assert mgr.as_array().dtype == np.int64
    mgr = create_mgr('c: i4; d: i2; e: u1')
    assert mgr.as_array().dtype == np.int32