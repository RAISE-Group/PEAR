def test_with_column_named_sparse(self):
    df = pd.DataFrame({'sparse': pd.arrays.SparseArray([1, 2])})
    assert isinstance(df.sparse, pd.core.arrays.sparse.accessor.SparseFrameAccessor)