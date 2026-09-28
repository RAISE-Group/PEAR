@pytest.mark.parametrize('vals', [[np.nan, np.nan, np.nan, np.nan, np.nan], [1, np.nan, np.nan, 3, np.nan], [1, np.nan, 0, 3, 0]])
@pytest.mark.parametrize('fill_value', [None, 0])
def test_dense_repr(self, vals, fill_value):
    vals = np.array(vals)
    arr = SparseArray(vals, fill_value=fill_value)
    res = arr.to_dense()
    tm.assert_numpy_array_equal(res, vals)
    res2 = arr._internal_get_values()
    tm.assert_numpy_array_equal(res2, vals)