def test_td64arr_div_tdlike_scalar_with_nat(self, two_hours, box_with_array):
    rng = TimedeltaIndex(['1 days', pd.NaT, '2 days'], name='foo')
    expected = pd.Float64Index([12, np.nan, 24], name='foo')
    rng = tm.box_expected(rng, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    result = rng / two_hours
    tm.assert_equal(result, expected)
    result = two_hours / rng
    expected = 1 / expected
    tm.assert_equal(result, expected)