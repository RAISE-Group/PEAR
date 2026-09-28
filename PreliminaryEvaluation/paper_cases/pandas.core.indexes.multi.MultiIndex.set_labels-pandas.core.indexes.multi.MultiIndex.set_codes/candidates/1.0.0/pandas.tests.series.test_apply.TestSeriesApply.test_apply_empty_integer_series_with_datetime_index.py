def test_apply_empty_integer_series_with_datetime_index(self):
    s = pd.Series([], index=pd.date_range(start='2018-01-01', periods=0), dtype=int)
    result = s.apply(lambda x: x)
    tm.assert_series_equal(result, s)