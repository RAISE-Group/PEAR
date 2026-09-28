def test_single_mgr_ctor(self):
    mgr = create_single_mgr('f8', num_rows=5)
    assert mgr.as_array().tolist() == [0.0, 1.0, 2.0, 3.0, 4.0]