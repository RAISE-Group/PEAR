def test_where_sparse(self):
    ser = pd.Series(pd.arrays.SparseArray([1, 2]))
    result = ser.where(ser >= 2, 0)
    expected = pd.Series(pd.arrays.SparseArray([0, 2]))
    tm.assert_series_equal(result, expected)