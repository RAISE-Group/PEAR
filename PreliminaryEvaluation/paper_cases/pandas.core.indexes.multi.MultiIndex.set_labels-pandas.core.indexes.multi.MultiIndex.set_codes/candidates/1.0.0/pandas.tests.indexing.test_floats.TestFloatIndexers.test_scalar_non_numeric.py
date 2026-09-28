def test_scalar_non_numeric(self):
    for index in [tm.makeStringIndex, tm.makeUnicodeIndex, tm.makeCategoricalIndex, tm.makeDateIndex, tm.makeTimedeltaIndex, tm.makePeriodIndex]:
        i = index(5)
        for s in [Series(np.arange(len(i)), index=i), DataFrame(np.random.randn(len(i), len(i)), index=i, columns=i)]:
            for idxr, getitem in [(lambda x: x.iloc, False), (lambda x: x, True)]:
                if getitem and isinstance(s, DataFrame):
                    error = KeyError
                    msg = '^3(\\.0)?$'
                else:
                    error = TypeError
                    msg = 'cannot do (label|index|positional) indexing on {klass} with these indexers \\[3\\.0\\] of {kind}|Cannot index by location index with a non-integer key'.format(klass=type(i), kind=str(float))
                with pytest.raises(error, match=msg):
                    idxr(s)[3.0]
            if s.index.inferred_type in {'categorical', 'string', 'unicode', 'mixed'}:
                error = KeyError
                msg = '^3$'
            else:
                error = TypeError
                msg = 'cannot do (label|index) indexing on {klass} with these indexers \\[3\\.0\\] of {kind}'.format(klass=type(i), kind=str(float))
            with pytest.raises(error, match=msg):
                s.loc[3.0]
            assert 3.0 not in s
            msg = 'cannot do (label|index|positional) indexing on {klass} with these indexers \\[3\\.0\\] of {kind}'.format(klass=type(i), kind=str(float))
            with pytest.raises(TypeError, match=msg):
                s.iloc[3.0] = 0
            if s.index.inferred_type in ['categorical']:
                pass
            elif s.index.inferred_type in ['datetime64', 'timedelta64', 'period']:
                pass
            else:
                s2 = s.copy()
                s2.loc[3.0] = 10
                assert s2.index.is_object()
                for idxr in [lambda x: x]:
                    s2 = s.copy()
                    idxr(s2)[3.0] = 0
                    assert s2.index.is_object()
        s = Series(np.arange(len(i)), index=i)
        s[3]
        msg = 'cannot do (label|index) indexing on {klass} with these indexers \\[3\\.0\\] of {kind}'.format(klass=type(i), kind=str(float))
        with pytest.raises(TypeError, match=msg):
            s[3.0]