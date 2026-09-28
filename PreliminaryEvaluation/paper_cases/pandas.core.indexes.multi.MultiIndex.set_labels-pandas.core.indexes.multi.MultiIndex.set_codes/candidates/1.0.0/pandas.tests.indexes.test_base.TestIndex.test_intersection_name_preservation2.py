@pytest.mark.parametrize('first_name,second_name,expected_name', [('A', 'A', 'A'), ('A', 'B', None), (None, 'B', None)])
@pytest.mark.parametrize('sort', [None, False])
def test_intersection_name_preservation2(self, index, first_name, second_name, expected_name, sort):
    first = index[5:20]
    second = index[:10]
    first.name = first_name
    second.name = second_name
    intersect = first.intersection(second, sort=sort)
    assert intersect.name == expected_name