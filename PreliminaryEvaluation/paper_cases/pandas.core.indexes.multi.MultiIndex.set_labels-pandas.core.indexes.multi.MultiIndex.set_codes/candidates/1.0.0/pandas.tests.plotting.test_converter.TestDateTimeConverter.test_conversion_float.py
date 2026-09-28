def test_conversion_float(self):
    decimals = 9
    rs = self.dtc.convert(Timestamp('2012-1-1 01:02:03', tz='UTC'), None, None)
    xp = converter.dates.date2num(Timestamp('2012-1-1 01:02:03', tz='UTC'))
    tm.assert_almost_equal(rs, xp, decimals)
    rs = self.dtc.convert(Timestamp('2012-1-1 09:02:03', tz='Asia/Hong_Kong'), None, None)
    tm.assert_almost_equal(rs, xp, decimals)
    rs = self.dtc.convert(datetime(2012, 1, 1, 1, 2, 3), None, None)
    tm.assert_almost_equal(rs, xp, decimals)