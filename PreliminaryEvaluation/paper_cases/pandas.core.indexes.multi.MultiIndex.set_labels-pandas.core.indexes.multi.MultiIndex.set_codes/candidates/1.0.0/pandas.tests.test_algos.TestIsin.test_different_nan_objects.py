def test_different_nan_objects(self):
    comps = np.array(['nan', np.nan * 1j, float('nan')], dtype=np.object)
    vals = np.array([float('nan')], dtype=np.object)
    expected = np.array([False, False, True])
    result = algos.isin(comps, vals)
    tm.assert_numpy_array_equal(expected, result)