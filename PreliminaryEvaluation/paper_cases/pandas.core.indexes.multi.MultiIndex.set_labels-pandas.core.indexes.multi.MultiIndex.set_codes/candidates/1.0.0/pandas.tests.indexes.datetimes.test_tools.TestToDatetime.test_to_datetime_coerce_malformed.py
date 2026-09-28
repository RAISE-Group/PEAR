def test_to_datetime_coerce_malformed(self):
    ts_strings = ['200622-12-31', '111111-24-11']
    result = to_datetime(ts_strings, errors='coerce')
    expected = Index([NaT, NaT])
    tm.assert_index_equal(result, expected)