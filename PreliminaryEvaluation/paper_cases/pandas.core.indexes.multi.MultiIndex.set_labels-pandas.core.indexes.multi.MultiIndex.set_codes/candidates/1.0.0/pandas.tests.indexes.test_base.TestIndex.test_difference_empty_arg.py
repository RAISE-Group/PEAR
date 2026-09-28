@pytest.mark.parametrize('sort', [None, False])
def test_difference_empty_arg(self, index, sort):
    first = index[5:20]
    first.name == 'name'
    result = first.difference([], sort)
    assert tm.equalContents(result, first)
    assert result.name == first.name