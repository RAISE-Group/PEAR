@pytest.mark.parametrize('cache', [True, False])
def test_unit_mixed(self, cache):
    expected = DatetimeIndex(['2013-01-01', 'NaT', 'NaT'])
    arr = [pd.Timestamp('20130101'), 1.434692e+18, 1.432766e+18]
    result = pd.to_datetime(arr, errors='coerce', cache=cache)
    tm.assert_index_equal(result, expected)
    with pytest.raises(ValueError):
        pd.to_datetime(arr, errors='raise', cache=cache)
    expected = DatetimeIndex(['NaT', 'NaT', '2013-01-01'])
    arr = [1.434692e+18, 1.432766e+18, pd.Timestamp('20130101')]
    result = pd.to_datetime(arr, errors='coerce', cache=cache)
    tm.assert_index_equal(result, expected)
    with pytest.raises(ValueError):
        pd.to_datetime(arr, errors='raise', cache=cache)