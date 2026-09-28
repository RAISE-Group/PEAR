def test_pi_add_iadd_int(self, one):
    rng = pd.period_range('2000-01-01 09:00', freq='H', periods=10)
    result = rng + one
    expected = pd.period_range('2000-01-01 10:00', freq='H', periods=10)
    tm.assert_index_equal(result, expected)
    rng += one
    tm.assert_index_equal(rng, expected)