def test_NaT_cast(self):
    result = Series([np.nan]).astype('period[D]')
    expected = Series([pd.NaT], dtype='period[D]')
    tm.assert_series_equal(result, expected)