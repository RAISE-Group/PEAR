def test_unique(self, indices):
    if isinstance(indices, (MultiIndex, CategoricalIndex)):
        pytest.skip('Skip check for MultiIndex/CategoricalIndex')
    expected = indices.drop_duplicates()
    for level in (0, indices.name, None):
        result = indices.unique(level=level)
        tm.assert_index_equal(result, expected)
    msg = 'Too many levels: Index has only 1 level, not 4'
    with pytest.raises(IndexError, match=msg):
        indices.unique(level=3)
    msg = f'Requested level \\(wrong\\) does not match index name \\({re.escape(indices.name.__repr__())}\\)'
    with pytest.raises(KeyError, match=msg):
        indices.unique(level='wrong')