def test_integer_positional_indexing(self):
    """ make sure that we are raising on positional indexing
        w.r.t. an integer index """
    s = Series(range(2, 6), index=range(2, 6))
    result = s[2:4]
    expected = s.iloc[2:4]
    tm.assert_series_equal(result, expected)
    for idxr in [lambda x: x, lambda x: x.iloc]:
        for l in [slice(2, 4.0), slice(2.0, 4), slice(2.0, 4.0)]:
            klass = RangeIndex
            msg = 'cannot do slice indexing on {klass} with these indexers \\[(2|4)\\.0\\] of {kind}'.format(klass=str(klass), kind=str(float))
            with pytest.raises(TypeError, match=msg):
                idxr(s)[l]