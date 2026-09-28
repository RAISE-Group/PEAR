@pytest.mark.parametrize('sort', [None, False])
def test_intersection_base(self, sort):
    index = self.create_index()
    first = index[:5]
    second = index[:3]
    expected = Index([0, 1, 'a']) if sort is None else Index([0, 'a', 1])
    result = first.intersection(second, sort=sort)
    tm.assert_index_equal(result, expected)