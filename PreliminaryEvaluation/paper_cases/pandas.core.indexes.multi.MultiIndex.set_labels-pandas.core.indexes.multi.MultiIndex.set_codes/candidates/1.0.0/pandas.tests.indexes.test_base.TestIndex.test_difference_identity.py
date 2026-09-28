@pytest.mark.parametrize('sort', [None, False])
def test_difference_identity(self, index, sort):
    first = index[5:20]
    first.name == 'name'
    result = first.difference(first, sort)
    assert len(result) == 0
    assert result.name == first.name