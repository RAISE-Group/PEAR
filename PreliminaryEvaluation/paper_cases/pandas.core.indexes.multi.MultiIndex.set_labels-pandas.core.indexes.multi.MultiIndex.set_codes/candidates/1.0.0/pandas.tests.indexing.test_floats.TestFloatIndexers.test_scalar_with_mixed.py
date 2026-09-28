def test_scalar_with_mixed(self):
    s2 = Series([1, 2, 3], index=['a', 'b', 'c'])
    s3 = Series([1, 2, 3], index=['a', 'b', 1.5])
    for idxr in [lambda x: x, lambda x: x.iloc]:
        msg = 'cannot do label indexing on {klass} with these indexers \\[1\\.0\\] of {kind}|Cannot index by location index with a non-integer key'.format(klass=str(Index), kind=str(float))
        with pytest.raises(TypeError, match=msg):
            idxr(s2)[1.0]
    with pytest.raises(KeyError, match='^1$'):
        s2.loc[1.0]
    result = s2.loc['b']
    expected = 2
    assert result == expected
    for idxr in [lambda x: x]:
        msg = 'cannot do label indexing on {klass} with these indexers \\[1\\.0\\] of {kind}'.format(klass=str(Index), kind=str(float))
        with pytest.raises(TypeError, match=msg):
            idxr(s3)[1.0]
        result = idxr(s3)[1]
        expected = 2
        assert result == expected
    msg = 'Cannot index by location index with a non-integer key'
    with pytest.raises(TypeError, match=msg):
        s3.iloc[1.0]
    with pytest.raises(KeyError, match='^1$'):
        s3.loc[1.0]
    result = s3.loc[1.5]
    expected = 3
    assert result == expected