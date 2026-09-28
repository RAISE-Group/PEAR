@pytest.mark.parametrize('data, categories', [(list('abcbca'), list('cab')), (pd.interval_range(0, 3).repeat(3), pd.interval_range(0, 3))], ids=['string', 'interval'])
def test_map_str(self, data, categories, ordered_fixture):
    index = CategoricalIndex(data, categories=categories, ordered=ordered_fixture)
    result = index.map(str)
    expected = CategoricalIndex(map(str, data), categories=map(str, categories), ordered=ordered_fixture)
    tm.assert_index_equal(result, expected)