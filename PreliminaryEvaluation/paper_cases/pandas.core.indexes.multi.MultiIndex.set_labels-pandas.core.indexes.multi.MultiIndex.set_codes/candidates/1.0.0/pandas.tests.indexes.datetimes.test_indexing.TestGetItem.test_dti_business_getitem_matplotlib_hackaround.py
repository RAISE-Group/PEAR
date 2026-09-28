def test_dti_business_getitem_matplotlib_hackaround(self):
    rng = pd.bdate_range(START, END)
    with tm.assert_produces_warning(DeprecationWarning):
        values = rng[:, None]
    expected = rng.values[:, None]
    tm.assert_numpy_array_equal(values, expected)