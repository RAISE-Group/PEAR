def test_grouper_index_types(self):
    df = DataFrame(np.arange(10).reshape(5, 2), columns=list('AB'))
    for index in [tm.makeFloatIndex, tm.makeStringIndex, tm.makeUnicodeIndex, tm.makeIntIndex, tm.makeDateIndex, tm.makePeriodIndex]:
        df.index = index(len(df))
        df.groupby(list('abcde')).apply(lambda x: x)
        df.index = list(reversed(df.index.tolist()))
        df.groupby(list('abcde')).apply(lambda x: x)