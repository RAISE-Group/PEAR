def test_util_testing_deprecated(self):
    sys.modules.pop('pandas.util.testing', None)
    with tm.assert_produces_warning(FutureWarning) as m:
        import pandas.util.testing
    assert 'pandas.util.testing is deprecated' in str(m[0].message)
    assert 'pandas.testing instead' in str(m[0].message)