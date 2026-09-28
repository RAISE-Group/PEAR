@pytest.mark.parametrize('dtype', ['int64', 'float64'])
@pytest.mark.parametrize('dense_index', [True, False])
@td.skip_if_no_scipy
def test_series_from_coo(self, dtype, dense_index):
    import scipy.sparse
    A = scipy.sparse.eye(3, format='coo', dtype=dtype)
    result = pd.Series.sparse.from_coo(A, dense_index=dense_index)
    index = pd.MultiIndex.from_tuples([(0, 0), (1, 1), (2, 2)])
    expected = pd.Series(SparseArray(np.array([1, 1, 1], dtype=dtype)), index=index)
    if dense_index:
        expected = expected.reindex(pd.MultiIndex.from_product(index.levels))
    tm.assert_series_equal(result, expected)