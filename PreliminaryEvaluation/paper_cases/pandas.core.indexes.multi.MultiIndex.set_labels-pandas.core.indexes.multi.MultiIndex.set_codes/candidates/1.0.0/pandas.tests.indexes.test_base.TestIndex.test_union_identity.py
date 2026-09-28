@pytest.mark.parametrize('sort', [None, False])
def test_union_identity(self, index, sort):
    first = index[5:20]
    union = first.union(first, sort=sort)
    assert (union is first) is (not sort)
    union = first.union([], sort=sort)
    assert (union is first) is (not sort)
    union = Index([]).union(first, sort=sort)
    assert (union is first) is (not sort)