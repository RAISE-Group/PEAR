@pytest.mark.parametrize('sort', [None, False])
def test_difference_sort(self, index, sort):
    first = index[5:20]
    second = index[:10]
    result = first.difference(second, sort)
    expected = index[10:20]
    if sort is None:
        expected = expected.sort_values()
    tm.assert_index_equal(result, expected)