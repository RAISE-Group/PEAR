@pytest.mark.parametrize('format', ['csc', 'csr', 'coo'])
@pytest.mark.parametrize('labels', [None, list(string.ascii_letters[:10])])
@pytest.mark.parametrize('dtype', ['float64', 'int64'])
@td.skip_if_no_scipy
def test_from_spmatrix(self, format, labels, dtype):
    import scipy.sparse
    sp_dtype = SparseDtype(dtype, np.array(0, dtype=dtype).item())
    mat = scipy.sparse.eye(10, format=format, dtype=dtype)
    result = pd.DataFrame.sparse.from_spmatrix(mat, index=labels, columns=labels)
    expected = pd.DataFrame(np.eye(10, dtype=dtype), index=labels, columns=labels).astype(sp_dtype)
    tm.assert_frame_equal(result, expected)