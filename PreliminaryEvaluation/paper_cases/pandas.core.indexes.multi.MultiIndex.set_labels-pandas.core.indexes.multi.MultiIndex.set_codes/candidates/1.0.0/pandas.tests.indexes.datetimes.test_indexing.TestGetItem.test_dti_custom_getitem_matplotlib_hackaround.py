def test_dti_custom_getitem_matplotlib_hackaround(self):
    rng = pd.bdate_range(START, END, freq='C')
    with tm.assert_produces_warning(DeprecationWarning):
        values = rng[:, None]
    expected = rng.values[:, None]
    tm.assert_numpy_array_equal(values, expected)