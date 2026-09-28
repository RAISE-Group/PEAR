def test_hongkong_tz_convert(self):
    dr = date_range('2012-01-01', '2012-01-10', freq='D', tz='Hongkong')
    dr.hour