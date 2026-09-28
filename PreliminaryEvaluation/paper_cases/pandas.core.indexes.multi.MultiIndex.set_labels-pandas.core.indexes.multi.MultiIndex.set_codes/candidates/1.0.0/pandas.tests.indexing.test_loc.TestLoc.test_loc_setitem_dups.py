def test_loc_setitem_dups(self):
    df_orig = DataFrame({'me': list('rttti'), 'foo': list('aaade'), 'bar': np.arange(5, dtype='float64') * 1.34 + 2, 'bar2': np.arange(5, dtype='float64') * -0.34 + 2}).set_index('me')
    indexer = tuple(['r', ['bar', 'bar2']])
    df = df_orig.copy()
    df.loc[indexer] *= 2.0
    tm.assert_series_equal(df.loc[indexer], 2.0 * df_orig.loc[indexer])
    indexer = tuple(['r', 'bar'])
    df = df_orig.copy()
    df.loc[indexer] *= 2.0
    assert df.loc[indexer] == 2.0 * df_orig.loc[indexer]
    indexer = tuple(['t', ['bar', 'bar2']])
    df = df_orig.copy()
    df.loc[indexer] *= 2.0
    tm.assert_frame_equal(df.loc[indexer], 2.0 * df_orig.loc[indexer])