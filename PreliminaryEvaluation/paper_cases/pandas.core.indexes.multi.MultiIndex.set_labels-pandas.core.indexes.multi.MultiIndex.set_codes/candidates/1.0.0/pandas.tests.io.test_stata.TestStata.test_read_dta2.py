def test_read_dta2(self):
    expected = DataFrame.from_records([(datetime(2006, 11, 19, 23, 13, 20), 1479596223000, datetime(2010, 1, 20), datetime(2010, 1, 8), datetime(2010, 1, 1), datetime(1974, 7, 1), datetime(2010, 1, 1), datetime(2010, 1, 1)), (datetime(1959, 12, 31, 20, 3, 20), -1479590, datetime(1953, 10, 2), datetime(1948, 6, 10), datetime(1955, 1, 1), datetime(1955, 7, 1), datetime(1955, 1, 1), datetime(2, 1, 1)), (pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT)], columns=['datetime_c', 'datetime_big_c', 'date', 'weekly_date', 'monthly_date', 'quarterly_date', 'half_yearly_date', 'yearly_date'])
    expected['yearly_date'] = expected['yearly_date'].astype('O')
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        parsed_114 = self.read_dta(self.dta2_114)
        parsed_115 = self.read_dta(self.dta2_115)
        parsed_117 = self.read_dta(self.dta2_117)
        w = [x for x in w if x.category is UserWarning]
        assert len(w) == 3
    tm.assert_frame_equal(parsed_114, expected, check_datetimelike_compat=True)
    tm.assert_frame_equal(parsed_115, expected, check_datetimelike_compat=True)
    tm.assert_frame_equal(parsed_117, expected, check_datetimelike_compat=True)