@pytest.mark.parametrize('fill_value', [0, None, np.nan])
def test_shift_fill_value(self, fill_value):
    sparse = SparseArray(np.array([1, 0, 0, 3, 0]), fill_value=8.0)
    res = sparse.shift(1, fill_value=fill_value)
    if isna(fill_value):
        fill_value = res.dtype.na_value
    exp = SparseArray(np.array([fill_value, 1, 0, 0, 3]), fill_value=8.0)
    tm.assert_sp_array_equal(res, exp)