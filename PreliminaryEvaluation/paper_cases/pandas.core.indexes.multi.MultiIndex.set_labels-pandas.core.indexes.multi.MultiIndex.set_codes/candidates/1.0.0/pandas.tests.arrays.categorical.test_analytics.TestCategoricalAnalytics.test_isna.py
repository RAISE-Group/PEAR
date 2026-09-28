def test_isna(self):
    exp = np.array([False, False, True])
    c = Categorical(['a', 'b', np.nan])
    res = c.isna()
    tm.assert_numpy_array_equal(res, exp)