def test_different_nans(self):
    comps = [float('nan')]
    values = [float('nan')]
    assert comps[0] is not values[0]
    result = algos.isin(comps, values)
    tm.assert_numpy_array_equal(np.array([True]), result)
    result = algos.isin(np.asarray(comps, dtype=np.object), np.asarray(values, dtype=np.object))
    tm.assert_numpy_array_equal(np.array([True]), result)
    result = algos.isin(np.asarray(comps, dtype=np.float64), np.asarray(values, dtype=np.float64))
    tm.assert_numpy_array_equal(np.array([True]), result)