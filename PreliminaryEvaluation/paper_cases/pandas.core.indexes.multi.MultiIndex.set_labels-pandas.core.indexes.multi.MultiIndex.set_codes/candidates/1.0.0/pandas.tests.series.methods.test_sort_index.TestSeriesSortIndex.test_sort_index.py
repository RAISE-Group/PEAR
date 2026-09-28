def test_sort_index(self, datetime_series):
    rindex = list(datetime_series.index)
    random.shuffle(rindex)
    random_order = datetime_series.reindex(rindex)
    sorted_series = random_order.sort_index()
    tm.assert_series_equal(sorted_series, datetime_series)
    sorted_series = random_order.sort_index(ascending=False)
    tm.assert_series_equal(sorted_series, datetime_series.reindex(datetime_series.index[::-1]))
    sorted_series = random_order.sort_index(level=0)
    tm.assert_series_equal(sorted_series, datetime_series)
    sorted_series = random_order.sort_index(axis=0)
    tm.assert_series_equal(sorted_series, datetime_series)
    msg = "No axis named 1 for object type <class 'pandas.core.series.Series'>"
    with pytest.raises(ValueError, match=msg):
        random_order.sort_values(axis=1)
    sorted_series = random_order.sort_index(level=0, axis=0)
    tm.assert_series_equal(sorted_series, datetime_series)
    with pytest.raises(ValueError, match=msg):
        random_order.sort_index(level=0, axis=1)