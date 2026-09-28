@pytest.mark.parametrize('index2,expected_arr', [(Index(['B', 'D']), ['B']), (Index(['B', 'D', 'A']), ['A', 'B', 'A'])])
@pytest.mark.parametrize('sort', [None, False])
def test_intersection_non_monotonic_non_unique(self, index2, expected_arr, sort):
    index1 = Index(['A', 'B', 'A', 'C'])
    expected = Index(expected_arr, dtype='object')
    result = index1.intersection(index2, sort=sort)
    if sort is None:
        expected = expected.sort_values()
    tm.assert_index_equal(result, expected)