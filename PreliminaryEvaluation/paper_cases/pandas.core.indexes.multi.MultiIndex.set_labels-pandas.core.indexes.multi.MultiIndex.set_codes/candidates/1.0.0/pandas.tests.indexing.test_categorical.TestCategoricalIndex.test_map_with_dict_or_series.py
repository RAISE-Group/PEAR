def test_map_with_dict_or_series(self):
    orig_values = ['a', 'B', 1, 'a']
    new_values = ['one', 2, 3.0, 'one']
    cur_index = pd.CategoricalIndex(orig_values, name='XXX')
    expected = pd.CategoricalIndex(new_values, name='XXX', categories=[3.0, 2, 'one'])
    mapper = pd.Series(new_values[:-1], index=orig_values[:-1])
    output = cur_index.map(mapper)
    tm.assert_index_equal(expected, output)
    mapper = {o: n for o, n in zip(orig_values[:-1], new_values[:-1])}
    output = cur_index.map(mapper)
    tm.assert_index_equal(expected, output)