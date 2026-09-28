@pytest.mark.parametrize('klass', [np.array, Series, list])
def test_union_different_type_base(self, klass):
    index = self.create_index()
    first = index[3:]
    second = index[:5]
    result = first.union(klass(second.values))
    assert tm.equalContents(result, index)