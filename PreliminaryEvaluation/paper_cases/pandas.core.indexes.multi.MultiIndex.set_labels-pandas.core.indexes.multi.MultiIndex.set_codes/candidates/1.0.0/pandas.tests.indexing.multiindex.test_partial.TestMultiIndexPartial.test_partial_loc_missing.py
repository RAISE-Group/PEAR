def test_partial_loc_missing(self, multiindex_year_month_day_dataframe_random_data):
    pytest.skip('skipping for now')
    ymd = multiindex_year_month_day_dataframe_random_data
    result = ymd.loc[2000, 0]
    expected = ymd.loc[2000]['A']
    tm.assert_series_equal(result, expected)
    with pytest.raises(Exception):
        ymd.loc[2000, 6]
    with pytest.raises(Exception):
        ymd.loc[(2000, 6), 0]