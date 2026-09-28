def test_series_loc_getitem_fancy(self, multiindex_year_month_day_dataframe_random_data):
    s = multiindex_year_month_day_dataframe_random_data['A']
    expected = s.reindex(s.index[49:51])
    result = s.loc[[(2000, 3, 10), (2000, 3, 13)]]
    tm.assert_series_equal(result, expected)