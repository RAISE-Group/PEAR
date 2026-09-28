@pytest.mark.parametrize('sort', [None, False])
def test_difference_base(self, sort):
    index = self.create_index()
    first = index[:4]
    second = index[3:]
    result = first.difference(second, sort)
    expected = Index([0, 'a', 1])
    if sort is None:
        expected = Index(safe_sort(expected))
    tm.assert_index_equal(result, expected)