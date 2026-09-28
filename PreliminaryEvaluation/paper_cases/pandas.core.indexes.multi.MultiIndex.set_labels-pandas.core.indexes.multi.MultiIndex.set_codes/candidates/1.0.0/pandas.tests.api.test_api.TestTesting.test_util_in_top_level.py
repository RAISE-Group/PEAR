def test_util_in_top_level(self):
    out = subprocess.check_output([sys.executable, '-c', 'import pandas; pandas.util.testing.assert_series_equal'], stderr=subprocess.STDOUT).decode()
    assert 'pandas.util.testing is deprecated' in out
    with pytest.raises(AttributeError, match='foo'):
        pd.util.foo