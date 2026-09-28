def test_constructor_maskedarray_hardened(self):
    data = ma.masked_all((3,), dtype=float).harden_mask()
    result = pd.Series(data)
    expected = pd.Series([np.nan, np.nan, np.nan])
    tm.assert_series_equal(result, expected)