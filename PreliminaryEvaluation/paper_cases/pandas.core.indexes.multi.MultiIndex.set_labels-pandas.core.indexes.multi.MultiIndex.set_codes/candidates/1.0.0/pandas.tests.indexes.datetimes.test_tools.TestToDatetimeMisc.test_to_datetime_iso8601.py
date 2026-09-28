@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_iso8601(self, cache):
    result = to_datetime(['2012-01-01 00:00:00'], cache=cache)
    exp = Timestamp('2012-01-01 00:00:00')
    assert result[0] == exp
    result = to_datetime(['20121001'], cache=cache)
    exp = Timestamp('2012-10-01')
    assert result[0] == exp