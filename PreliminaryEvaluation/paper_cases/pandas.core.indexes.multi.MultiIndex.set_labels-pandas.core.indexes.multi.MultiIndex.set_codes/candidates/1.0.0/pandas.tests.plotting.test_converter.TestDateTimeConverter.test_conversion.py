def test_conversion(self):
    rs = self.dtc.convert(['2012-1-1'], None, None)[0]
    xp = datetime(2012, 1, 1).toordinal()
    assert rs == xp
    rs = self.dtc.convert('2012-1-1', None, None)
    assert rs == xp
    rs = self.dtc.convert(date(2012, 1, 1), None, None)
    assert rs == xp
    rs = self.dtc.convert(datetime(2012, 1, 1).toordinal(), None, None)
    assert rs == xp
    rs = self.dtc.convert('2012-1-1', None, None)
    assert rs == xp
    rs = self.dtc.convert(Timestamp('2012-1-1'), None, None)
    assert rs == xp
    rs = self.dtc.convert(np_datetime64_compat('2012-01-01'), None, None)
    assert rs == xp
    rs = self.dtc.convert(np_datetime64_compat('2012-01-01 00:00:00+0000'), None, None)
    assert rs == xp
    rs = self.dtc.convert(np.array([np_datetime64_compat('2012-01-01 00:00:00+0000'), np_datetime64_compat('2012-01-02 00:00:00+0000')]), None, None)
    assert rs[0] == xp
    ts = Timestamp('2012-01-01').tz_localize('UTC').tz_convert('US/Eastern')
    rs = self.dtc.convert(ts, None, None)
    assert rs == xp
    rs = self.dtc.convert(ts.to_pydatetime(), None, None)
    assert rs == xp
    rs = self.dtc.convert(Index([ts - Day(1), ts]), None, None)
    assert rs[1] == xp
    rs = self.dtc.convert(Index([ts - Day(1), ts]).to_pydatetime(), None, None)
    assert rs[1] == xp