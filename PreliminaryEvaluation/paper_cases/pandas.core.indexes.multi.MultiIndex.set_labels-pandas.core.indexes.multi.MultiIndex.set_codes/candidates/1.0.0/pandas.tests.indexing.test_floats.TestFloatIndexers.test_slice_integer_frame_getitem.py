def test_slice_integer_frame_getitem(self):
    for index in [Int64Index(range(5)), RangeIndex(5)]:
        s = DataFrame(np.random.randn(5, 2), index=index)

        def f(idxr):
            for l in [slice(0.0, 1), slice(0, 1.0), slice(0.0, 1.0)]:
                result = idxr(s)[l]
                indexer = slice(0, 2)
                self.check(result, s, indexer, False)
                msg = 'cannot do slice indexing on {klass} with these indexers \\[(0|1)\\.0\\] of {kind}'.format(klass=type(index), kind=str(float))
                with pytest.raises(TypeError, match=msg):
                    s[l]
            for l in [slice(-10, 10), slice(-10.0, 10.0)]:
                result = idxr(s)[l]
                self.check(result, s, slice(-10, 10), True)
            msg = 'cannot do slice indexing on {klass} with these indexers \\[-10\\.0\\] of {kind}'.format(klass=type(index), kind=str(float))
            with pytest.raises(TypeError, match=msg):
                s[slice(-10.0, 10.0)]
            for l, res in [(slice(0.5, 1), slice(1, 2)), (slice(0, 0.5), slice(0, 1)), (slice(0.5, 1.5), slice(1, 2))]:
                result = idxr(s)[l]
                self.check(result, s, res, False)
                msg = 'cannot do slice indexing on {klass} with these indexers \\[0\\.5\\] of {kind}'.format(klass=type(index), kind=str(float))
                with pytest.raises(TypeError, match=msg):
                    s[l]
            for l in [slice(3.0, 4), slice(3, 4.0), slice(3.0, 4.0)]:
                sc = s.copy()
                idxr(sc)[l] = 0
                result = idxr(sc)[l].values.ravel()
                assert (result == 0).all()
                msg = 'cannot do slice indexing on {klass} with these indexers \\[(3|4)\\.0\\] of {kind}'.format(klass=type(index), kind=str(float))
                with pytest.raises(TypeError, match=msg):
                    s[l] = 0
        f(lambda x: x.loc)