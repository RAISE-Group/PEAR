@pytest.mark.parametrize('tz_range', [pd.date_range('2013-01-01 05:00:00Z', periods=2), pd.date_range('2013-01-01 00:00:00', periods=2, tz='US/Eastern'), pd.date_range('2013-01-01 00:00:00-0500', periods=2)])
def test_tz_range_is_utc(self, tz_range):
    from pandas.io.json import dumps
    exp = '["2013-01-01T05:00:00.000Z","2013-01-02T05:00:00.000Z"]'
    dfexp = '{"DT":{"0":"2013-01-01T05:00:00.000Z","1":"2013-01-02T05:00:00.000Z"}}'
    assert dumps(tz_range, iso_dates=True) == exp
    dti = pd.DatetimeIndex(tz_range)
    assert dumps(dti, iso_dates=True) == exp
    df = DataFrame({'DT': dti})
    result = dumps(df, iso_dates=True)
    assert result == dfexp