@td.skip_if_no_scipy
def test_to_coo(self):
    import scipy.sparse
    df = pd.DataFrame({'A': [0, 1, 0], 'B': [1, 0, 0]}, dtype='Sparse[int64, 0]')
    result = df.sparse.to_coo()
    expected = scipy.sparse.coo_matrix(np.asarray(df))
    assert (result != expected).nnz == 0