@pytest.mark.parametrize('first_list', [list('ba'), list()])
@pytest.mark.parametrize('second_list', [list('ab'), list()])
@pytest.mark.parametrize('first_name, second_name, expected_name', [('A', 'B', None), (None, 'B', None), ('A', None, None)])
@pytest.mark.parametrize('sort', [None, False])
def test_union_name_preservation(self, first_list, second_list, first_name, second_name, expected_name, sort):
    first = Index(first_list, name=first_name)
    second = Index(second_list, name=second_name)
    union = first.union(second, sort=sort)
    vals = set(first_list).union(second_list)
    if sort is None and len(first_list) > 0 and (len(second_list) > 0):
        expected = Index(sorted(vals), name=expected_name)
        tm.assert_index_equal(union, expected)
    else:
        expected = Index(vals, name=expected_name)
        assert tm.equalContents(union, expected)