def test_constructor_from_index_series_datetimetz(self):
    idx = date_range('2015-01-01 10:00', freq='D', periods=3, tz='US/Eastern')
    result = Categorical(idx)
    tm.assert_index_equal(result.categories, idx)
    result = Categorical(Series(idx))
    tm.assert_index_equal(result.categories, idx)