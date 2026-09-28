def test_dti_shift_int(self):
    rng = date_range('1/1/2000', periods=20)
    result = rng + 5 * rng.freq
    expected = rng.shift(5)
    tm.assert_index_equal(result, expected)
    result = rng - 5 * rng.freq
    expected = rng.shift(-5)
    tm.assert_index_equal(result, expected)