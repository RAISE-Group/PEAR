def test_map_with_tuples_mi(self):
    first_level = ['foo', 'bar', 'baz']
    multi_index = MultiIndex.from_tuples(zip(first_level, [1, 2, 3]))
    reduced_index = multi_index.map(lambda x: x[0])
    tm.assert_index_equal(reduced_index, Index(first_level))