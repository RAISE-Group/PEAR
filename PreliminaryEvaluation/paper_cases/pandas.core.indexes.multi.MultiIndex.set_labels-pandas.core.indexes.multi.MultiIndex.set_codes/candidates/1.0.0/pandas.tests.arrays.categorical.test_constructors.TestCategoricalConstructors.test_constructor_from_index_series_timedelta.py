def test_constructor_from_index_series_timedelta(self):
    idx = timedelta_range('1 days', freq='D', periods=3)
    result = Categorical(idx)
    tm.assert_index_equal(result.categories, idx)
    result = Categorical(Series(idx))
    tm.assert_index_equal(result.categories, idx)