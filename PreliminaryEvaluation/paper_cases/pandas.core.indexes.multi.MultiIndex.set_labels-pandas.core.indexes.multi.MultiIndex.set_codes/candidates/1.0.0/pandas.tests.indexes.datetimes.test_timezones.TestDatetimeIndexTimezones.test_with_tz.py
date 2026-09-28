@pytest.mark.parametrize('tz', [pytz.timezone('US/Central'), gettz('US/Central')])
def test_with_tz(self, tz):
    start = datetime(2011, 3, 12, tzinfo=pytz.utc)
    dr = bdate_range(start, periods=50, freq=pd.offsets.Hour())
    assert dr.tz is pytz.utc
    dr = bdate_range('1/1/2005', '1/1/2009', tz=pytz.utc)
    dr = bdate_range('1/1/2005', '1/1/2009', tz=tz)
    central = dr.tz_convert(tz)
    assert central.tz is tz
    naive = central[0].to_pydatetime().replace(tzinfo=None)
    comp = conversion.localize_pydatetime(naive, tz).tzinfo
    assert central[0].tz is comp
    naive = dr[0].to_pydatetime().replace(tzinfo=None)
    comp = conversion.localize_pydatetime(naive, tz).tzinfo
    assert central[0].tz is comp
    dr = bdate_range(datetime(2005, 1, 1, tzinfo=pytz.utc), datetime(2009, 1, 1, tzinfo=pytz.utc))
    with pytest.raises(Exception):
        bdate_range(datetime(2005, 1, 1, tzinfo=pytz.utc), '1/1/2009', tz=tz)