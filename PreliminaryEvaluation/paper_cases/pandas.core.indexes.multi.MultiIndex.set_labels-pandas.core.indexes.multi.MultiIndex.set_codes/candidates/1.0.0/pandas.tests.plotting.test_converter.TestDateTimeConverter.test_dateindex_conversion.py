def test_dateindex_conversion(self):
    decimals = 9
    for freq in ('B', 'L', 'S'):
        dateindex = tm.makeDateIndex(k=10, freq=freq)
        rs = self.dtc.convert(dateindex, None, None)
        xp = converter.dates.date2num(dateindex._mpl_repr())
        tm.assert_almost_equal(rs, xp, decimals)