@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_format_time(self, cache):
    data = [['01/10/2010 15:20', '%m/%d/%Y %H:%M', Timestamp('2010-01-10 15:20')], ['01/10/2010 05:43', '%m/%d/%Y %I:%M', Timestamp('2010-01-10 05:43')], ['01/10/2010 13:56:01', '%m/%d/%Y %H:%M:%S', Timestamp('2010-01-10 13:56:01')]]
    for s, format, dt in data:
        assert to_datetime(s, format=format, cache=cache) == dt