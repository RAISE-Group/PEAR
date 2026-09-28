def test_sort_index_kind(self):
    series = Series(index=[3, 2, 1, 4, 3], dtype=object)
    expected_series = Series(index=[1, 2, 3, 3, 4], dtype=object)
    index_sorted_series = series.sort_index(kind='mergesort')
    tm.assert_series_equal(expected_series, index_sorted_series)
    index_sorted_series = series.sort_index(kind='quicksort')
    tm.assert_series_equal(expected_series, index_sorted_series)
    index_sorted_series = series.sort_index(kind='heapsort')
    tm.assert_series_equal(expected_series, index_sorted_series)