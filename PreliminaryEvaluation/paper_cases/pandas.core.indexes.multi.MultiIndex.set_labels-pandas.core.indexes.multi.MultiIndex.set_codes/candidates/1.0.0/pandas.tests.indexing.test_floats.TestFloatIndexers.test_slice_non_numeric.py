def test_slice_non_numeric(self):
    for index in [tm.makeStringIndex, tm.makeUnicodeIndex, tm.makeDateIndex, tm.makeTimedeltaIndex, tm.makePeriodIndex]:
        index = index(5)
        for s in [Series(range(5), index=index), DataFrame(np.random.randn(5, 2), index=index)]:
            for l in [slice(3.0, 4), slice(3, 4.0), slice(3.0, 4.0)]:
                msg = 'cannot do slice indexing on {klass} with these indexers \\[(3|4)\\.0\\] of {kind}'.format(klass=type(index), kind=str(float))
                with pytest.raises(TypeError, match=msg):
                    s.iloc[l]
                for idxr in [lambda x: x.loc, lambda x: x.iloc, lambda x: x]:
                    msg = 'cannot do slice indexing on {klass} with these indexers \\[(3|4)(\\.0)?\\] of ({kind_float}|{kind_int})'.format(klass=type(index), kind_float=str(float), kind_int=str(int))
                    with pytest.raises(TypeError, match=msg):
                        idxr(s)[l]
            for l in [slice(3.0, 4), slice(3, 4.0), slice(3.0, 4.0)]:
                msg = 'cannot do slice indexing on {klass} with these indexers \\[(3|4)\\.0\\] of {kind}'.format(klass=type(index), kind=str(float))
                with pytest.raises(TypeError, match=msg):
                    s.iloc[l] = 0
                for idxr in [lambda x: x.loc, lambda x: x.iloc, lambda x: x]:
                    msg = 'cannot do slice indexing on {klass} with these indexers \\[(3|4)(\\.0)?\\] of ({kind_float}|{kind_int})'.format(klass=type(index), kind_float=str(float), kind_int=str(int))
                    with pytest.raises(TypeError, match=msg):
                        idxr(s)[l] = 0