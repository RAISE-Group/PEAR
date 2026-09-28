def test_sort_index_inplace(self, datetime_series):
    rindex = list(datetime_series.index)
    random.shuffle(rindex)
    random_order = datetime_series.reindex(rindex)
    result = random_order.sort_index(ascending=False, inplace=True)
    assert result is None
    tm.assert_series_equal(random_order, datetime_series.reindex(datetime_series.index[::-1]))
    random_order = datetime_series.reindex(rindex)
    result = random_order.sort_index(ascending=True, inplace=True)
    assert result is None
    tm.assert_series_equal(random_order, datetime_series)