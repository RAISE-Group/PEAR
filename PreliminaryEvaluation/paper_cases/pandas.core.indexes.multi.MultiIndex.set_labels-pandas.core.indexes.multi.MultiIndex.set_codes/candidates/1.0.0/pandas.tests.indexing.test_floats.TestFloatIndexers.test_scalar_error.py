def test_scalar_error(self):
    for index in [tm.makeStringIndex, tm.makeUnicodeIndex, tm.makeCategoricalIndex, tm.makeDateIndex, tm.makeTimedeltaIndex, tm.makePeriodIndex, tm.makeIntIndex, tm.makeRangeIndex]:
        i = index(5)
        s = Series(np.arange(len(i)), index=i)
        msg = 'Cannot index by location index'
        with pytest.raises(TypeError, match=msg):
            s.iloc[3.0]
        msg = 'cannot do positional indexing on {klass} with these indexers \\[3\\.0\\] of {kind}'.format(klass=type(i), kind=str(float))
        with pytest.raises(TypeError, match=msg):
            s.iloc[3.0] = 0