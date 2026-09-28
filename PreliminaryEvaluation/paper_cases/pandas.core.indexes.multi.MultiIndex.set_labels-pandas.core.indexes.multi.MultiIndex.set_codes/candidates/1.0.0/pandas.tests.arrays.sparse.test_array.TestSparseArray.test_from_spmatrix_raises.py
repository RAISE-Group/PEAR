@td.skip_if_no_scipy
def test_from_spmatrix_raises(self):
    import scipy.sparse
    mat = scipy.sparse.eye(5, 4, format='csc')
    with pytest.raises(ValueError, match="not '4'"):
        SparseArray.from_spmatrix(mat)