@pytest.mark.parametrize('format', ['coo', 'csc', 'csr'])
@pytest.mark.parametrize('size', [pytest.param(0, marks=td.skip_if_np_lt('1.16', reason='NumPy-11383')), 10])
@td.skip_if_no_scipy
def test_from_spmatrix(self, size, format):
    import scipy.sparse
    mat = scipy.sparse.random(size, 1, density=0.5, format=format)
    result = SparseArray.from_spmatrix(mat)
    result = np.asarray(result)
    expected = mat.toarray().ravel()
    tm.assert_numpy_array_equal(result, expected)