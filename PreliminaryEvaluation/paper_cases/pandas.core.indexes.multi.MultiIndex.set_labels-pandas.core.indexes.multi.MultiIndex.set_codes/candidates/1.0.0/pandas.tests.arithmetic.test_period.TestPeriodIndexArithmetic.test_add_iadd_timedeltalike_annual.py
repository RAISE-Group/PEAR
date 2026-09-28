def test_add_iadd_timedeltalike_annual(self):
    rng = pd.period_range('2014', '2024', freq='A')
    result = rng + pd.offsets.YearEnd(5)
    expected = pd.period_range('2019', '2029', freq='A')
    tm.assert_index_equal(result, expected)
    rng += pd.offsets.YearEnd(5)
    tm.assert_index_equal(rng, expected)