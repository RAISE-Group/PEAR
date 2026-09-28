def test_isin_nan_common_object(self, nulls_fixture, nulls_fixture2):
    if isinstance(nulls_fixture, float) and isinstance(nulls_fixture2, float) and math.isnan(nulls_fixture) and math.isnan(nulls_fixture2):
        tm.assert_numpy_array_equal(Index(['a', nulls_fixture]).isin([nulls_fixture2]), np.array([False, True]))
    elif nulls_fixture is nulls_fixture2:
        tm.assert_numpy_array_equal(Index(['a', nulls_fixture]).isin([nulls_fixture2]), np.array([False, True]))
    else:
        tm.assert_numpy_array_equal(Index(['a', nulls_fixture]).isin([nulls_fixture2]), np.array([False, False]))