@pytest.mark.parametrize('tzstr', ['US/Eastern', 'dateutil/US/Eastern'])
def test_dti_shift_localized(self, tzstr):
    dr = date_range('2011/1/1', '2012/1/1', freq='W-FRI')
    dr_tz = dr.tz_localize(tzstr)
    result = dr_tz.shift(1, '10T')
    assert result.tz == dr_tz.tz