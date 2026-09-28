@pytest.mark.parametrize('columns', [['a', 'b'], pd.MultiIndex.from_product([['A'], ['a', 'b']]), ['a', 'a']])
@td.skip_if_no_scipy
def test_from_spmatrix_columns(self, columns):
    import scipy.sparse
    dtype = SparseDtype('float64', 0.0)
    mat = scipy.sparse.random(10, 2, density=0.5)
    result = pd.DataFrame.sparse.from_spmatrix(mat, columns=columns)
    expected = pd.DataFrame(mat.toarray(), columns=columns).astype(dtype)
    tm.assert_frame_equal(result, expected)