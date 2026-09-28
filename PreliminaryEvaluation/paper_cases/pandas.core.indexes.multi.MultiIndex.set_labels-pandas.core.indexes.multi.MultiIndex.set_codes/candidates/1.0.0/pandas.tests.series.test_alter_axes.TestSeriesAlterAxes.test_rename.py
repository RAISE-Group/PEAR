def test_rename(self, datetime_series):
    ts = datetime_series
    renamer = lambda x: x.strftime('%Y%m%d')
    renamed = ts.rename(renamer)
    assert renamed.index[0] == renamer(ts.index[0])
    rename_dict = dict(zip(ts.index, renamed.index))
    renamed2 = ts.rename(rename_dict)
    tm.assert_series_equal(renamed, renamed2)
    s = Series(np.arange(4), index=['a', 'b', 'c', 'd'], dtype='int64')
    renamed = s.rename({'b': 'foo', 'd': 'bar'})
    tm.assert_index_equal(renamed.index, Index(['a', 'foo', 'c', 'bar']))
    renamer = Series(np.arange(4), index=Index(['a', 'b', 'c', 'd'], name='name'), dtype='int64')
    renamed = renamer.rename({})
    assert renamed.index.name == renamer.index.name