@pytest.mark.parametrize('ts', [Timestamp('2013-01-10 05:00:00Z'), Timestamp('2013-01-10 00:00:00', tz='US/Eastern'), Timestamp('2013-01-10 00:00:00-0500')])
def test_tz_is_utc(self, ts):
    from pandas.io.json import dumps
    exp = '"2013-01-10T05:00:00.000Z"'
    assert dumps(ts, iso_dates=True) == exp
    dt = ts.to_pydatetime()
    assert dumps(dt, iso_dates=True) == exp