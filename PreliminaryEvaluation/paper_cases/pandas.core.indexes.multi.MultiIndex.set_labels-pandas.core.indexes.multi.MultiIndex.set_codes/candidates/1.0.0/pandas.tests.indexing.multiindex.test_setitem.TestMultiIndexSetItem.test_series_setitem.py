def test_series_setitem(self, multiindex_year_month_day_dataframe_random_data):
    ymd = multiindex_year_month_day_dataframe_random_data
    s = ymd['A']
    s[2000, 3] = np.nan
    assert isna(s.values[42:65]).all()
    assert notna(s.values[:42]).all()
    assert notna(s.values[65:]).all()
    s[2000, 3, 10] = np.nan
    assert isna(s[49])