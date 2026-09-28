def test_as_array_float(self):
    mgr = create_mgr('c: f4; d: f2; e: f8')
    assert mgr.as_array().dtype == np.float64
    mgr = create_mgr('c: f4; d: f2')
    assert mgr.as_array().dtype == np.float32