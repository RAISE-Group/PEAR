def test_constructor_arrays_negative_year(self):
    years = np.arange(1960, 2000, dtype=np.int64).repeat(4)
    quarters = np.tile(np.array([1, 2, 3, 4], dtype=np.int64), 40)
    pindex = PeriodIndex(year=years, quarter=quarters)
    tm.assert_index_equal(pindex.year, pd.Index(years))
    tm.assert_index_equal(pindex.quarter, pd.Index(quarters))