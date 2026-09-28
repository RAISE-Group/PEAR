def test_scientific_no_exponent(self):
    arr = np.array(['42E', '2E', '99e', '6e'], dtype='O')
    result = lib.maybe_convert_numeric(arr, set(), False, True)
    assert np.all(np.isnan(result))