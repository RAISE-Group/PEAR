@pytest.mark.parametrize('cache', [True, False])
def test_unit_with_numeric(self, cache):
    expected = DatetimeIndex(['2015-06-19 05:33:20', '2015-05-27 22:33:20'])
    arr1 = [1.434692e+18, 1.432766e+18]
    arr2 = np.array(arr1).astype('int64')
    for errors in ['ignore', 'raise', 'coerce']:
        result = pd.to_datetime(arr1, errors=errors, cache=cache)
        tm.assert_index_equal(result, expected)
        result = pd.to_datetime(arr2, errors=errors, cache=cache)
        tm.assert_index_equal(result, expected)
    expected = DatetimeIndex(['NaT', '2015-06-19 05:33:20', '2015-05-27 22:33:20'])
    arr = ['foo', 1.434692e+18, 1.432766e+18]
    result = pd.to_datetime(arr, errors='coerce', cache=cache)
    tm.assert_index_equal(result, expected)
    expected = DatetimeIndex(['2015-06-19 05:33:20', '2015-05-27 22:33:20', 'NaT', 'NaT'])
    arr = [1.434692e+18, 1.432766e+18, 'foo', 'NaT']
    result = pd.to_datetime(arr, errors='coerce', cache=cache)
    tm.assert_index_equal(result, expected)