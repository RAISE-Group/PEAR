def test_constructor_year_and_quarter(self):
    year = pd.Series([2001, 2002, 2003])
    quarter = year - 2000
    idx = PeriodIndex(year=year, quarter=quarter)
    strs = ['{t[0]:d}Q{t[1]:d}'.format(t=t) for t in zip(quarter, year)]
    lops = list(map(Period, strs))
    p = PeriodIndex(lops)
    tm.assert_index_equal(p, idx)