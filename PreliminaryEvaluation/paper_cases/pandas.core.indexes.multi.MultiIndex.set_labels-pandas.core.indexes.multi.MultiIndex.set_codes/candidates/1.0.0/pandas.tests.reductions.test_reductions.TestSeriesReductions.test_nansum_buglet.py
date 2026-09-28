def test_nansum_buglet(self):
    ser = Series([1.0, np.nan], index=[0, 1])
    result = np.nansum(ser)
    tm.assert_almost_equal(result, 1)