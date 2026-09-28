def test_datetime_understood(self):
    series = pd.Series(pd.date_range('2012-01-01', periods=3))
    offset = pd.offsets.DateOffset(days=6)
    result = series - offset
    expected = pd.Series(pd.to_datetime(['2011-12-26', '2011-12-27', '2011-12-28']))
    tm.assert_series_equal(result, expected)