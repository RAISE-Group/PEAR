def test_scalar_float(self):
    index = Index(np.arange(5.0))
    for s in [Series(np.arange(len(index)), index=index), DataFrame(np.random.randn(len(index), len(index)), index=index, columns=index)]:
        indexer = index[3]
        for idxr, getitem in [(lambda x: x.loc, False), (lambda x: x, True)]:
            result = idxr(s)[indexer]
            self.check(result, s, 3, getitem)
            s2 = s.copy()
            result = idxr(s2)[indexer]
            self.check(result, s, 3, getitem)
            with pytest.raises(KeyError, match='^3\\.5$'):
                idxr(s)[3.5]
        assert 3.0 in s
        expected = s.iloc[3]
        s2 = s.copy()
        s2.iloc[3] = expected
        result = s2.iloc[3]
        self.check(result, s, 3, False)
        msg = 'Cannot index by location index with a non-integer key'
        with pytest.raises(TypeError, match=msg):
            s.iloc[3.0]
        msg = 'cannot do positional indexing on {klass} with these indexers \\[3\\.0\\] of {kind}'.format(klass=str(Float64Index), kind=str(float))
        with pytest.raises(TypeError, match=msg):
            s2.iloc[3.0] = 0