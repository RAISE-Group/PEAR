def test_reset_index(self, float_frame):
    stacked = float_frame.stack()[::2]
    stacked = DataFrame({'foo': stacked, 'bar': stacked})
    names = ['first', 'second']
    stacked.index.names = names
    deleveled = stacked.reset_index()
    for i, (lev, level_codes) in enumerate(zip(stacked.index.levels, stacked.index.codes)):
        values = lev.take(level_codes)
        name = names[i]
        tm.assert_index_equal(values, Index(deleveled[name]))
    stacked.index.names = [None, None]
    deleveled2 = stacked.reset_index()
    tm.assert_series_equal(deleveled['first'], deleveled2['level_0'], check_names=False)
    tm.assert_series_equal(deleveled['second'], deleveled2['level_1'], check_names=False)
    rdf = float_frame.reset_index()
    exp = Series(float_frame.index.values, name='index')
    tm.assert_series_equal(rdf['index'], exp)
    df = float_frame.copy()
    df['index'] = 'foo'
    rdf = df.reset_index()
    exp = Series(float_frame.index.values, name='level_0')
    tm.assert_series_equal(rdf['level_0'], exp)
    float_frame.index.name = 'index'
    deleveled = float_frame.reset_index()
    tm.assert_series_equal(deleveled['index'], Series(float_frame.index))
    tm.assert_index_equal(deleveled.index, Index(np.arange(len(deleveled))))
    float_frame.columns.name = 'columns'
    resetted = float_frame.reset_index()
    assert resetted.columns.name == 'columns'
    df = float_frame.reset_index().set_index(['index', 'A', 'B'])
    rs = df.reset_index(['A', 'B'])
    tm.assert_frame_equal(rs, float_frame, check_names=False)
    rs = df.reset_index(['index', 'A', 'B'])
    tm.assert_frame_equal(rs, float_frame.reset_index(), check_names=False)
    rs = df.reset_index(['index', 'A', 'B'])
    tm.assert_frame_equal(rs, float_frame.reset_index(), check_names=False)
    rs = df.reset_index('A')
    xp = float_frame.reset_index().set_index(['index', 'B'])
    tm.assert_frame_equal(rs, xp, check_names=False)
    df = float_frame.copy()
    resetted = float_frame.reset_index()
    df.reset_index(inplace=True)
    tm.assert_frame_equal(df, resetted, check_names=False)
    df = float_frame.reset_index().set_index(['index', 'A', 'B'])
    rs = df.reset_index('A', drop=True)
    xp = float_frame.copy()
    del xp['A']
    xp = xp.set_index(['B'], append=True)
    tm.assert_frame_equal(rs, xp, check_names=False)