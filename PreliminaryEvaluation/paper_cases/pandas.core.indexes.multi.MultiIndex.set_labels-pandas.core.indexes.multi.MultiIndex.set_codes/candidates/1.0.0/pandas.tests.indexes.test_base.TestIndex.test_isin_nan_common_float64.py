def test_isin_nan_common_float64(self, nulls_fixture):
    if nulls_fixture is pd.NaT:
        pytest.skip('pd.NaT not compatible with Float64Index')
    tm.assert_numpy_array_equal(Float64Index([1.0, nulls_fixture]).isin([np.nan]), np.array([False, True]))
    tm.assert_numpy_array_equal(Float64Index([1.0, nulls_fixture]).isin([pd.NaT]), np.array([False, False]))