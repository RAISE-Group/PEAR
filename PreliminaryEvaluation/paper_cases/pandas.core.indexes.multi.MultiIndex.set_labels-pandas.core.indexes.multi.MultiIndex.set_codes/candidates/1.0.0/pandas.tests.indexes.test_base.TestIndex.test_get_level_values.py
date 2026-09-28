@pytest.mark.parametrize('name,level', [(None, 0), ('a', 'a')])
def test_get_level_values(self, index, name, level):
    expected = index.copy()
    if name:
        expected.name = name
    result = expected.get_level_values(level)
    tm.assert_index_equal(result, expected)