@pytest.mark.parametrize('klass', [np.array, Series, list])
@pytest.mark.parametrize('sort', [None, False])
def test_intersection_different_type_base(self, klass, sort):
    index = self.create_index()
    first = index[:5]
    second = index[:3]
    result = first.intersection(klass(second.values), sort=sort)
    assert tm.equalContents(result, second)