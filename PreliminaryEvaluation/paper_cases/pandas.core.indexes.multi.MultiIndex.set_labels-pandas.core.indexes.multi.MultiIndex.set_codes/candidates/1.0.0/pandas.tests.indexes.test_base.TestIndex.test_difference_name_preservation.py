@pytest.mark.parametrize('second_name,expected', [(None, None), ('name', 'name')])
@pytest.mark.parametrize('sort', [None, False])
def test_difference_name_preservation(self, index, second_name, expected, sort):
    first = index[5:20]
    second = index[:10]
    answer = index[10:20]
    first.name = 'name'
    second.name = second_name
    result = first.difference(second, sort=sort)
    assert tm.equalContents(result, answer)
    if expected is None:
        assert result.name is None
    else:
        assert result.name == expected