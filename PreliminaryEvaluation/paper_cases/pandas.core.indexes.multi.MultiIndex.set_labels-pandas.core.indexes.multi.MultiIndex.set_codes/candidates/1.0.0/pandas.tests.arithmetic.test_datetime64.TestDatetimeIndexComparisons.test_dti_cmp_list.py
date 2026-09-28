def test_dti_cmp_list(self):
    rng = date_range('1/1/2000', periods=10)
    result = rng == list(rng)
    expected = rng == rng
    tm.assert_numpy_array_equal(result, expected)