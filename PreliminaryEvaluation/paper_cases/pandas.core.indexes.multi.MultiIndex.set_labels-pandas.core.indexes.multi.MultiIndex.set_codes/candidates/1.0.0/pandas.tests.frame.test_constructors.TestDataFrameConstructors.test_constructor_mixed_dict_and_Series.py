def test_constructor_mixed_dict_and_Series(self):
    data = {}
    data['A'] = {'foo': 1, 'bar': 2, 'baz': 3}
    data['B'] = Series([4, 3, 2, 1], index=['bar', 'qux', 'baz', 'foo'])
    result = DataFrame(data)
    assert result.index.is_monotonic
    with pytest.raises(ValueError, match='ambiguous ordering'):
        DataFrame({'A': ['a', 'b'], 'B': {'a': 'a', 'b': 'b'}})
    result = DataFrame({'A': ['a', 'b'], 'B': Series(['a', 'b'], index=['a', 'b'])})
    expected = DataFrame({'A': ['a', 'b'], 'B': ['a', 'b']}, index=['a', 'b'])
    tm.assert_frame_equal(result, expected)