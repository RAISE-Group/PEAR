def test_at_to_fail(self):
    s = Series([1, 2, 3], index=list('abc'))
    result = s.at['a']
    assert result == 1
    msg = 'At based indexing on an non-integer index can only have non-integer indexers'
    with pytest.raises(ValueError, match=msg):
        s.at[0]
    df = DataFrame({'A': [1, 2, 3]}, index=list('abc'))
    result = df.at['a', 'A']
    assert result == 1
    with pytest.raises(ValueError, match=msg):
        df.at['a', 0]
    s = Series([1, 2, 3], index=[3, 2, 1])
    result = s.at[1]
    assert result == 3
    msg = 'At based indexing on an integer index can only have integer indexers'
    with pytest.raises(ValueError, match=msg):
        s.at['a']
    df = DataFrame({0: [1, 2, 3]}, index=[3, 2, 1])
    result = df.at[1, 0]
    assert result == 3
    with pytest.raises(ValueError, match=msg):
        df.at['a', 0]
    df = DataFrame({'x': [1.0], 'y': [2.0], 'z': [3.0]})
    df.columns = ['x', 'x', 'z']
    with pytest.raises(KeyError, match="\\['y'\\] not in index"):
        df[['x', 'y', 'z']]