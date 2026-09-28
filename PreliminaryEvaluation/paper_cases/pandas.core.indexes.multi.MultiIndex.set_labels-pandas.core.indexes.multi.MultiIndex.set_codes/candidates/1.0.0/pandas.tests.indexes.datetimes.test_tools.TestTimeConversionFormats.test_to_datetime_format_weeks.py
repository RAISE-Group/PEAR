@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_format_weeks(self, cache):
    data = [['2009324', '%Y%W%w', Timestamp('2009-08-13')], ['2013020', '%Y%U%w', Timestamp('2013-01-13')]]
    for s, format, dt in data:
        assert to_datetime(s, format=format, cache=cache) == dt