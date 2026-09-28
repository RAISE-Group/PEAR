def test_fillna_float64(self):
    idx = Index([1.0, np.nan, 3.0], dtype=float, name='x')
    exp = Index([1.0, 0.1, 3.0], name='x')
    tm.assert_index_equal(idx.fillna(0.1), exp)
    exp = Float64Index([1.0, 2.0, 3.0], name='x')
    tm.assert_index_equal(idx.fillna(2), exp)
    exp = Index([1.0, 'obj', 3.0], name='x')
    tm.assert_index_equal(idx.fillna('obj'), exp)