@td.skip_if_has_locale
@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_with_non_exact(self, cache):
    s = Series(['19MAY11', 'foobar19MAY11', '19MAY11:00:00:00', '19MAY11 00:00:00Z'])
    result = to_datetime(s, format='%d%b%y', exact=False, cache=cache)
    expected = to_datetime(s.str.extract('(\\d+\\w+\\d+)', expand=False), format='%d%b%y', cache=cache)
    tm.assert_series_equal(result, expected)