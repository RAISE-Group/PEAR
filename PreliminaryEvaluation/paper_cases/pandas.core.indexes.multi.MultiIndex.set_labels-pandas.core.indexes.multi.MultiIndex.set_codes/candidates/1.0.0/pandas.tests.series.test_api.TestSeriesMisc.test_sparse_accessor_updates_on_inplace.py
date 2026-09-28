def test_sparse_accessor_updates_on_inplace(self):
    s = pd.Series([1, 1, 2, 3], dtype='Sparse[int]')
    s.drop([0, 1], inplace=True)
    assert s.sparse.density == 1.0