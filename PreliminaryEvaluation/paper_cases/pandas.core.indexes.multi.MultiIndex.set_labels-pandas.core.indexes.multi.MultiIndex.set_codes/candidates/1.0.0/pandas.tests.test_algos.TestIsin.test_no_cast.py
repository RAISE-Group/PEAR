def test_no_cast(self):
    comps = ['ss', 42]
    values = ['42']
    expected = np.array([False, False])
    result = algos.isin(comps, values)
    tm.assert_numpy_array_equal(expected, result)