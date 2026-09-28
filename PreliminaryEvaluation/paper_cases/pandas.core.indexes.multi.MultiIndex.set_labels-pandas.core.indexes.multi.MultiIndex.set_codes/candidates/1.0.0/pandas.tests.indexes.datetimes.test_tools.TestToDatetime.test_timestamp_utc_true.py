@pytest.mark.parametrize('ts, expected', [(Timestamp('2018-01-01'), Timestamp('2018-01-01', tz='UTC')), (Timestamp('2018-01-01', tz='US/Pacific'), Timestamp('2018-01-01 08:00', tz='UTC'))])
def test_timestamp_utc_true(self, ts, expected):
    result = to_datetime(ts, utc=True)
    assert result == expected