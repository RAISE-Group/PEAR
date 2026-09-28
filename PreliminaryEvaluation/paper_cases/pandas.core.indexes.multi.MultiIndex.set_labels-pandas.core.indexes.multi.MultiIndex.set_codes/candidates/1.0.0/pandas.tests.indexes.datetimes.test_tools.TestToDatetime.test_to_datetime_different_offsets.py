@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_different_offsets(self, cache):
    ts_string_1 = 'March 1, 2018 12:00:00+0400'
    ts_string_2 = 'March 1, 2018 12:00:00+0500'
    arr = [ts_string_1] * 5 + [ts_string_2] * 5
    expected = pd.Index([parse(x) for x in arr])
    result = pd.to_datetime(arr, cache=cache)
    tm.assert_index_equal(result, expected)