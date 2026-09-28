def test_mpl_compat_hack(self, datetime_series):
    with tm.assert_produces_warning(None):
        result = datetime_series[:, np.newaxis]
    expected = datetime_series.values[:, np.newaxis]
    tm.assert_almost_equal(result, expected)