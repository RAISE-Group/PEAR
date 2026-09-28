def test_categorical_nan_equality(self):
    cat = Series(Categorical(['a', 'b', 'c', np.nan]))
    exp = Series([True, True, True, False])
    res = cat == cat
    tm.assert_series_equal(res, exp)