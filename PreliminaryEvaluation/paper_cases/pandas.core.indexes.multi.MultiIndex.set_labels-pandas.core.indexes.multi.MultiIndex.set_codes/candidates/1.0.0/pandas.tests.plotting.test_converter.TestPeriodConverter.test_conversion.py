def test_conversion(self):
    rs = self.pc.convert(['2012-1-1'], None, self.axis)[0]
    xp = Period('2012-1-1').ordinal
    assert rs == xp
    rs = self.pc.convert('2012-1-1', None, self.axis)
    assert rs == xp
    rs = self.pc.convert([date(2012, 1, 1)], None, self.axis)[0]
    assert rs == xp
    rs = self.pc.convert(date(2012, 1, 1), None, self.axis)
    assert rs == xp
    rs = self.pc.convert([Timestamp('2012-1-1')], None, self.axis)[0]
    assert rs == xp
    rs = self.pc.convert(Timestamp('2012-1-1'), None, self.axis)
    assert rs == xp
    rs = self.pc.convert(np_datetime64_compat('2012-01-01'), None, self.axis)
    assert rs == xp
    rs = self.pc.convert(np_datetime64_compat('2012-01-01 00:00:00+0000'), None, self.axis)
    assert rs == xp
    rs = self.pc.convert(np.array([np_datetime64_compat('2012-01-01 00:00:00+0000'), np_datetime64_compat('2012-01-02 00:00:00+0000')]), None, self.axis)
    assert rs[0] == xp