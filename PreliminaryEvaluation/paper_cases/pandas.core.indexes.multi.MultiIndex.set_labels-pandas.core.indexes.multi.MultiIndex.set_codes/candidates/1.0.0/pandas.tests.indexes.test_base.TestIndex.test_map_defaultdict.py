def test_map_defaultdict(self):
    index = Index([1, 2, 3])
    default_dict = defaultdict(lambda: 'blank')
    default_dict[1] = 'stuff'
    result = index.map(default_dict)
    expected = Index(['stuff', 'blank', 'blank'])
    tm.assert_index_equal(result, expected)