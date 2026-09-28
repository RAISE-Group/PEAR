@td.skip_if_no_scipy
def test_series_from_coo_incorrect_format_raises(self):
    import scipy.sparse
    m = scipy.sparse.csr_matrix(np.array([[0, 1], [0, 0]]))
    with pytest.raises(TypeError, match='Expected coo_matrix. Got csr_matrix instead.'):
        pd.Series.sparse.from_coo(m)