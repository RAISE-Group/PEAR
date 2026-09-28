@td.xfail_non_writeable
def test_put_mixed_type(self, setup_path):
    df = tm.makeTimeDataFrame()
    df['obj1'] = 'foo'
    df['obj2'] = 'bar'
    df['bool1'] = df['A'] > 0
    df['bool2'] = df['B'] > 0
    df['bool3'] = True
    df['int1'] = 1
    df['int2'] = 2
    df['timestamp1'] = Timestamp('20010102')
    df['timestamp2'] = Timestamp('20010103')
    df['datetime1'] = datetime.datetime(2001, 1, 2, 0, 0)
    df['datetime2'] = datetime.datetime(2001, 1, 3, 0, 0)
    df.loc[3:6, ['obj1']] = np.nan
    df = df._consolidate()._convert(datetime=True)
    with ensure_clean_store(setup_path) as store:
        _maybe_remove(store, 'df')
        with catch_warnings(record=True):
            simplefilter('ignore', pd.errors.PerformanceWarning)
            store.put('df', df)
        expected = store.get('df')
        tm.assert_frame_equal(expected, df)