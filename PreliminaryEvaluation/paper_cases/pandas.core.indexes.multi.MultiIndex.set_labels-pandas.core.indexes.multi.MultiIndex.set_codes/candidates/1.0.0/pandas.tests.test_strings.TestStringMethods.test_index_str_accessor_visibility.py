def test_index_str_accessor_visibility(self):
    from pandas.core.strings import StringMethods
    cases = [(['a', 'b'], 'string'), (['a', 'b', 1], 'mixed-integer'), (['a', 'b', 1.3], 'mixed'), (['a', 'b', 1.3, 1], 'mixed-integer'), (['aa', datetime(2011, 1, 1)], 'mixed')]
    for values, tp in cases:
        idx = Index(values)
        assert isinstance(Series(values).str, StringMethods)
        assert isinstance(idx.str, StringMethods)
        assert idx.inferred_type == tp
    for values, tp in cases:
        idx = Index(values)
        assert isinstance(Series(values).str, StringMethods)
        assert isinstance(idx.str, StringMethods)
        assert idx.inferred_type == tp
    cases = [([1, np.nan], 'floating'), ([datetime(2011, 1, 1)], 'datetime64'), ([timedelta(1)], 'timedelta64')]
    for values, tp in cases:
        idx = Index(values)
        message = 'Can only use .str accessor with string values'
        with pytest.raises(AttributeError, match=message):
            Series(values).str
        with pytest.raises(AttributeError, match=message):
            idx.str
        assert idx.inferred_type == tp
    idx = MultiIndex.from_tuples([('a', 'b'), ('a', 'b')])
    assert idx.inferred_type == 'mixed'
    message = 'Can only use .str accessor with Index, not MultiIndex'
    with pytest.raises(AttributeError, match=message):
        idx.str