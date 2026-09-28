def test_util_testing_deprecated_direct(self):
    sys.modules.pop('pandas.util.testing', None)
    with tm.assert_produces_warning(FutureWarning) as m:
        from pandas.util.testing import assert_series_equal
    assert 'pandas.util.testing is deprecated' in str(m[0].message)
    assert 'pandas.testing instead' in str(m[0].message)