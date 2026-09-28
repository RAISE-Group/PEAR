@pytest.mark.parametrize('data, non_lexsorted_data', [[[1, 2, 3], [9, 0, 1, 2, 3]], [list('abc'), list('fabcd')]])
def test_is_monotonic(self, data, non_lexsorted_data):
    c = CategoricalIndex(data)
    assert c.is_monotonic_increasing is True
    assert c.is_monotonic_decreasing is False
    c = CategoricalIndex(data, ordered=True)
    assert c.is_monotonic_increasing is True
    assert c.is_monotonic_decreasing is False
    c = CategoricalIndex(data, categories=reversed(data))
    assert c.is_monotonic_increasing is False
    assert c.is_monotonic_decreasing is True
    c = CategoricalIndex(data, categories=reversed(data), ordered=True)
    assert c.is_monotonic_increasing is False
    assert c.is_monotonic_decreasing is True
    reordered_data = [data[0], data[2], data[1]]
    c = CategoricalIndex(reordered_data, categories=reversed(data))
    assert c.is_monotonic_increasing is False
    assert c.is_monotonic_decreasing is False
    categories = non_lexsorted_data
    c = CategoricalIndex(categories[:2], categories=categories)
    assert c.is_monotonic_increasing is True
    assert c.is_monotonic_decreasing is False
    c = CategoricalIndex(categories[1:3], categories=categories)
    assert c.is_monotonic_increasing is True
    assert c.is_monotonic_decreasing is False