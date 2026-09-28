def test_nan_multiple_containment(self):
    i = Float64Index([1.0, np.nan])
    tm.assert_numpy_array_equal(i.isin([1.0]), np.array([True, False]))
    tm.assert_numpy_array_equal(i.isin([2.0, np.pi]), np.array([False, False]))
    tm.assert_numpy_array_equal(i.isin([np.nan]), np.array([False, True]))
    tm.assert_numpy_array_equal(i.isin([1.0, np.nan]), np.array([True, True]))
    i = Float64Index([1.0, 2.0])
    tm.assert_numpy_array_equal(i.isin([np.nan]), np.array([False, False]))