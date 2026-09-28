def test_has_duplicates(self, indices):
    holder = type(indices)
    if not len(indices) or isinstance(indices, (MultiIndex, RangeIndex)):
        pytest.skip('Skip check for empty Index, MultiIndex, and RangeIndex')
    idx = holder([indices[0]] * 5)
    assert idx.is_unique is False
    assert idx.has_duplicates is True