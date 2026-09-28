@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_with_space_in_series(self, cache):
    s = Series(['10/18/2006', '10/18/2008', ' '])
    msg = "(\\(')?String does not contain a date(:', ' '\\))?"
    with pytest.raises(ValueError, match=msg):
        to_datetime(s, errors='raise', cache=cache)
    result_coerce = to_datetime(s, errors='coerce', cache=cache)
    expected_coerce = Series([datetime(2006, 10, 18), datetime(2008, 10, 18), NaT])
    tm.assert_series_equal(result_coerce, expected_coerce)
    result_ignore = to_datetime(s, errors='ignore', cache=cache)
    tm.assert_series_equal(result_ignore, s)