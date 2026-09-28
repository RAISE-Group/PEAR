@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_on_datetime64_series(self, cache):
    s = Series(date_range('1/1/2000', periods=10))
    result = to_datetime(s, cache=cache)
    assert result[0] == s[0]