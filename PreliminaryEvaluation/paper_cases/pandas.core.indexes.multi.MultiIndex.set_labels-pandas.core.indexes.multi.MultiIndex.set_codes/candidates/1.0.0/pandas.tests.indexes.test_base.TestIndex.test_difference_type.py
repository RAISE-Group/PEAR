@pytest.mark.parametrize('sort', [None, False])
def test_difference_type(self, indices, sort):
    if not indices.is_unique:
        return
    result = indices.difference(indices, sort=sort)
    expected = indices.drop(indices)
    tm.assert_index_equal(result, expected)