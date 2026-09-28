@pytest.mark.parametrize('value', [1, 'True', [1, 2, 3], 5.0])
def test_validate_inplace_raises(self, value):
    cat = Categorical(['A', 'B', 'B', 'C', 'A'])
    msg = f'For argument "inplace" expected type bool, received type {type(value).__name__}'
    with pytest.raises(ValueError, match=msg):
        cat.set_ordered(value=True, inplace=value)
    with pytest.raises(ValueError, match=msg):
        cat.as_ordered(inplace=value)
    with pytest.raises(ValueError, match=msg):
        cat.as_unordered(inplace=value)
    with pytest.raises(ValueError, match=msg):
        cat.set_categories(['X', 'Y', 'Z'], rename=True, inplace=value)
    with pytest.raises(ValueError, match=msg):
        cat.rename_categories(['X', 'Y', 'Z'], inplace=value)
    with pytest.raises(ValueError, match=msg):
        cat.reorder_categories(['X', 'Y', 'Z'], ordered=True, inplace=value)
    with pytest.raises(ValueError, match=msg):
        cat.add_categories(new_categories=['D', 'E', 'F'], inplace=value)
    with pytest.raises(ValueError, match=msg):
        cat.remove_categories(removals=['D', 'E', 'F'], inplace=value)
    with pytest.raises(ValueError, match=msg):
        cat.remove_unused_categories(inplace=value)
    with pytest.raises(ValueError, match=msg):
        cat.sort_values(inplace=value)