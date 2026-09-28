def test_slice_integer(self):
    for index, oob in [(Int64Index(range(5)), False), (RangeIndex(5), False), (Int64Index(range(5)) + 10, True)]:
        s = Series(range(5), index=index)
        for l in [slice(3.0, 4), slice(3, 4.0), slice(3.0, 4.0)]:
            for idxr in [lambda x: x.loc]:
                result = idxr(s)[l]
                if oob:
                    indexer = slice(0, 0)
                else:
                    indexer = slice(3, 5)
                self.check(result, s, indexer, False)
            msg = 'cannot do slice indexing on {klass} with these indexers \\[(3|4)\\.0\\] of {kind}'.format(klass=type(index), kind=str(float))
            with pytest.raises(TypeError, match=msg):
                s[l]
        for l in [slice(-6, 6), slice(-6.0, 6.0)]:
            for idxr in [lambda x: x.loc]:
                result = idxr(s)[l]
                if oob:
                    indexer = slice(0, 0)
                else:
                    indexer = slice(-6, 6)
                self.check(result, s, indexer, False)
        msg = 'cannot do slice indexing on {klass} with these indexers \\[-6\\.0\\] of {kind}'.format(klass=type(index), kind=str(float))
        with pytest.raises(TypeError, match=msg):
            s[slice(-6.0, 6.0)]
        for l, res1 in [(slice(2.5, 4), slice(3, 5)), (slice(2, 3.5), slice(2, 4)), (slice(2.5, 3.5), slice(3, 4))]:
            for idxr in [lambda x: x.loc]:
                result = idxr(s)[l]
                if oob:
                    res = slice(0, 0)
                else:
                    res = res1
                self.check(result, s, res, False)
            msg = 'cannot do slice indexing on {klass} with these indexers \\[(2|3)\\.5\\] of {kind}'.format(klass=type(index), kind=str(float))
            with pytest.raises(TypeError, match=msg):
                s[l]
        for l in [slice(3.0, 4), slice(3, 4.0), slice(3.0, 4.0)]:
            for idxr in [lambda x: x.loc]:
                sc = s.copy()
                idxr(sc)[l] = 0
                result = idxr(sc)[l].values.ravel()
                assert (result == 0).all()
            msg = 'cannot do slice indexing on {klass} with these indexers \\[(3|4)\\.0\\] of {kind}'.format(klass=type(index), kind=str(float))
            with pytest.raises(TypeError, match=msg):
                s[l] = 0