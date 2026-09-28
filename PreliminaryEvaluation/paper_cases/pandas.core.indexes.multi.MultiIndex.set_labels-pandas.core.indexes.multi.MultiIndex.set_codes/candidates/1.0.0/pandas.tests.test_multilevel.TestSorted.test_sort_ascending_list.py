def test_sort_ascending_list(self):
    arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'], [4, 3, 2, 1, 4, 3, 2, 1]]
    tuples = zip(*arrays)
    mi = MultiIndex.from_tuples(tuples, names=['first', 'second', 'third'])
    s = Series(range(8), index=mi)
    result = s.sort_index(level=['third', 'first'], ascending=False)
    expected = s.iloc[[4, 0, 5, 1, 6, 2, 7, 3]]
    tm.assert_series_equal(result, expected)
    result = s.sort_index(level=['third', 'first'], ascending=[False, True])
    expected = s.iloc[[0, 4, 1, 5, 2, 6, 3, 7]]
    tm.assert_series_equal(result, expected)