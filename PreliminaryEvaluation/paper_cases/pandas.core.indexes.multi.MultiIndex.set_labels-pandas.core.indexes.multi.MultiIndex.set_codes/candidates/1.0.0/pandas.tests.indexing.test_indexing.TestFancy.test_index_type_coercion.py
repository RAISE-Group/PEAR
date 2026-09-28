def test_index_type_coercion(self):
    for s in [Series(range(5)), Series(range(5), index=range(1, 6))]:
        assert s.index.is_integer()
        for indexer in [lambda x: x.loc, lambda x: x]:
            s2 = s.copy()
            indexer(s2)[0.1] = 0
            assert s2.index.is_floating()
            assert indexer(s2)[0.1] == 0
            s2 = s.copy()
            indexer(s2)[0.0] = 0
            exp = s.index
            if 0 not in s:
                exp = Index(s.index.tolist() + [0])
            tm.assert_index_equal(s2.index, exp)
            s2 = s.copy()
            indexer(s2)['0'] = 0
            assert s2.index.is_object()
    for s in [Series(range(5), index=np.arange(5.0))]:
        assert s.index.is_floating()
        for idxr in [lambda x: x.loc, lambda x: x]:
            s2 = s.copy()
            idxr(s2)[0.1] = 0
            assert s2.index.is_floating()
            assert idxr(s2)[0.1] == 0
            s2 = s.copy()
            idxr(s2)[0.0] = 0
            tm.assert_index_equal(s2.index, s.index)
            s2 = s.copy()
            idxr(s2)['0'] = 0
            assert s2.index.is_object()