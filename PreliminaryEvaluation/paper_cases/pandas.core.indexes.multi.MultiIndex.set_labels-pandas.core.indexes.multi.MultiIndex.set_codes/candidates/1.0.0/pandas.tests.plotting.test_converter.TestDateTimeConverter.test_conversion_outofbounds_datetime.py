def test_conversion_outofbounds_datetime(self):
    values = [date(1677, 1, 1), date(1677, 1, 2)]
    rs = self.dtc.convert(values, None, None)
    xp = converter.dates.date2num(values)
    tm.assert_numpy_array_equal(rs, xp)
    rs = self.dtc.convert(values[0], None, None)
    xp = converter.dates.date2num(values[0])
    assert rs == xp
    values = [datetime(1677, 1, 1, 12), datetime(1677, 1, 2, 12)]
    rs = self.dtc.convert(values, None, None)
    xp = converter.dates.date2num(values)
    tm.assert_numpy_array_equal(rs, xp)
    rs = self.dtc.convert(values[0], None, None)
    xp = converter.dates.date2num(values[0])
    assert rs == xp