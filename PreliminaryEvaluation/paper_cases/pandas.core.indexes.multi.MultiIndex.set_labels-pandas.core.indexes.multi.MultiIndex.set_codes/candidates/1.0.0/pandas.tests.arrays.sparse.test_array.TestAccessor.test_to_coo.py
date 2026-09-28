@td.skip_if_no_scipy
def test_to_coo(self):
    import scipy.sparse
    ser = pd.Series([1, 2, 3], index=pd.MultiIndex.from_product([[0], [1, 2, 3]], names=['a', 'b']), dtype='Sparse[int]')
    A, _, _ = ser.sparse.to_coo()
    assert isinstance(A, scipy.sparse.coo.coo_matrix)