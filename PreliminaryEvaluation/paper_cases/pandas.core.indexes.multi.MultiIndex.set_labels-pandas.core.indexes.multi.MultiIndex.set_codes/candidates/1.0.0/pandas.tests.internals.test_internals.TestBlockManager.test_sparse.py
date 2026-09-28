def test_sparse(self):
    mgr = create_mgr('a: sparse-1; b: sparse-2')
    assert mgr.as_array().dtype == np.float64