@pytest.mark.parametrize('sort', [None, False])
def test_intersection_difference(self, indices, sort):
    if not indices.is_unique:
        return
    inter = indices.intersection(indices.drop(indices))
    diff = indices.difference(indices, sort=sort)
    tm.assert_index_equal(inter, diff)