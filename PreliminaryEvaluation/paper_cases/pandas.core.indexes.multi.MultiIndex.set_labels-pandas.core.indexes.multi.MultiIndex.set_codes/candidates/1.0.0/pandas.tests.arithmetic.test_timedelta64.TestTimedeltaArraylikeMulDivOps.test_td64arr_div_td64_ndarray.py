def test_td64arr_div_td64_ndarray(self, box_with_array):
    rng = TimedeltaIndex(['1 days', pd.NaT, '2 days'])
    expected = pd.Float64Index([12, np.nan, 24])
    rng = tm.box_expected(rng, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    other = np.array([2, 4, 2], dtype='m8[h]')
    result = rng / other
    tm.assert_equal(result, expected)
    result = rng / tm.box_expected(other, box_with_array)
    tm.assert_equal(result, expected)
    result = rng / other.astype(object)
    tm.assert_equal(result, expected)
    result = rng / list(other)
    tm.assert_equal(result, expected)
    expected = 1 / expected
    result = other / rng
    tm.assert_equal(result, expected)
    result = tm.box_expected(other, box_with_array) / rng
    tm.assert_equal(result, expected)
    result = other.astype(object) / rng
    tm.assert_equal(result, expected)
    result = list(other) / rng
    tm.assert_equal(result, expected)