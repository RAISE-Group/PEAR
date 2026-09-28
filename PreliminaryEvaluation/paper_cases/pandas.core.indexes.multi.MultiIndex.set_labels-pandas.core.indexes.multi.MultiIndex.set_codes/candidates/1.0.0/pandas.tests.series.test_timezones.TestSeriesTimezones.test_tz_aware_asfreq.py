@pytest.mark.parametrize('tz', ['US/Eastern', 'dateutil/US/Eastern'])
def test_tz_aware_asfreq(self, tz):
    dr = date_range('2011-12-01', '2012-07-20', freq='D', tz=tz)
    ser = Series(np.random.randn(len(dr)), index=dr)
    ser.asfreq('T')